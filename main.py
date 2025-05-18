#from functions import get_todos, write_todos
import functions

# Variables
todos_file = 'todos.txt'
# Menu
optMenu = """
========== Operation ===========
1. Add          4. Complete
2. Show         5. Exit
3. Edit
"""

# Greeting message
print("\nHi! Welcome to Todo List App\n")

# Create todos list from a text file
todos = functions.get_todos(todos_file)

while True:
    # Main menu loop
    while True:
        print(optMenu)
        user_action = input("Select an operation with number 1-5: ")
        if functions.isValid_intInput(user_action,1,5):
            user_action = int(user_action)
            print("\n")
            break
        else:
            print("!!! Invalid input !!!")

    match user_action:
        case 1:
            # Add operation
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)

            functions.write_todos(todos_file, todos)

        case 2:
            # Show operation
            print("========== To-Do List ==========")
            toShow = [todo.strip("\n") for todo in todos]

            for index, item in enumerate(toShow):
                row = f"{index + 1}-{item}"
                print(row)
        case 3:
            # Edit operation
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos_file, todos)
        case 4:
            # Complete operation
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)

            functions.write_todos(todos_file, todos)
        case 5:
            # Exit operation
            break
        case _:
            print("Please input 1-5.")

print("\nGoodbye!\n")