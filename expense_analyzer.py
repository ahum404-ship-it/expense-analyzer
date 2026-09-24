def classify_expense(amount):
    if amount < 25:
        return "small"
    elif amount <= 100:
        return "moderate"
    else:
        return "large"


def main():
    expenses = []

    while True:
        entry = input("Enter an expense or 0 to finish: ")
        amount = float(entry)

        if amount == 0:
            break

        if amount < 0:
            print("Expense cannot be negative. Please try again.")
            continue

        expenses.append(amount)

    if len(expenses) == 0:
        print("No expenses entered.")
        return

    small_count = 0
    moderate_count = 0
    large_count = 0

    for expense in expenses:
        category = classify_expense(expense)
        if category == "small":
            small_count += 1
        elif category == "moderate":
            moderate_count += 1
        else:
            large_count += 1

    total = sum(expenses)
    average = total / len(expenses)
    smallest = min(expenses)
    largest = max(expenses)

    print()
    print("Expense Summary")
    print("---------------")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total: ${total:,.2f}")
    print(f"Average: ${average:,.2f}")
    print(f"Smallest expense: ${smallest:,.2f}")
    print(f"Largest expense: ${largest:,.2f}")
    print(f"Small expenses: {small_count}")
    print(f"Moderate expenses: {moderate_count}")
    print(f"Large expenses: {large_count}")


if __name__ == "__main__":
    main()
