import json

def load_data():
    try:
        with open("expenses.txt", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def save_data(data):
    with open("expenses.txt", "w") as file:
        json.dump(data, file)

def add_expense(category, amount):
    expenses = load_data()
    expenses.append({"category" : category, "amount" : amount})
    save_data(expenses)

def view_by_category(category):
    expenses = load_data()
    for expense in expenses:
        if expense["category"] == category:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}")

def view_total_expense():
    expenses = load_data()
    total = sum(item['amount'] for item in expenses)
    print(f"Total Expense: {total}")


def main():
    while True:
        expenses = load_data()
        print("Welcome to expense tracker: \n" \
        "1. Add an expense \n"
        "2. View by category \n" \
        "3. view total expense \n" \
        "4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            category = input("Enter the category of expense (e.g., food, travel, utilities): ")
            amount = float(input("Enter the amount: "))
            add_expense(category, amount)
        elif choice == 2:
            category = input("Enter the category to view expenses: ")
            view_by_category(category)
        elif choice == 3:
            view_total_expense()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()