# Personal Mini-Toolkit
# A beginner-friendly collection of three useful tools.

# Tool 1: Calculate two numbers using a chosen operation.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))

        print("Choose an operation: +, -, *, /")
        operation = input("Your operation: ").strip()

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif operation == "/":
            if second == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = first / second
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: Manage a to-do list that changes while the program runs.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    number = int(input("Enter the task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Removed task: {removed}")
                    else:
                        print("That task number does not exist.")
                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


# Tool 3: Check whether a number is even or odd.
def even_number_checker():
    print("\n--- Even Number Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Main menu: Repeat until the user chooses to quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\nChoose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Even Number Checker")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            even_number_checker()
        elif choice == "4":
            print("Thank you for using My Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
# Start the program.
if __name__ == "__main__":
    main()