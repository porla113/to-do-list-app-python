# Greeting message
print("\nHi! Welcome to Todo List App\n")

# Create todos list from a text file
with open('todos.txt', 'r') as file:
    todos = file.readlines()

# Menu
optMenu = """
========== Operation ===========
1. Add          4. Complete
2. Show         5. Exit
3. Edit
"""

while True:
    print(optMenu)
    user_action = int(input("Select an operation with number 1-5: "))
    print("\n")

    match user_action:
        case 1:
            # Add operation
            todo = input("Enter a todo: ") + "\n"
            
            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

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

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 4:
            # Complete operation
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 5:
            # Exit operation
            break
        case _:
            print("Please input 1-5.")

print("\nGoodbye!\n")