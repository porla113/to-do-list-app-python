# Variables
todos_file = 'todos.txt'
# Menu
optMenu = """
========== Operation ===========
1. Add          4. Complete
2. Show         5. Exit
3. Edit
"""
# Functions
# get_todos function
def get_todos(filepath):
    """
    Open and read from a file
    Arguments:
    - filepath - string
    Return:
    - a list of string
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

# set_todos function
def set_todos(filepath, todos_list):
    """
    Write a string list to a file
    Arguments:
    - filepath: string
    - todos_list: a list of string
    Return:
    - None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)

# Greeting message
print("\nHi! Welcome to Todo List App\n")

# Create todos list from a text file
todos = get_todos(todos_file)
print(type(todos))
while True:
    print(optMenu)
    user_action = int(input("Select an operation with number 1-5: "))
    print("\n")

    match user_action:
        case 1:
            # Add operation
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)

            set_todos(todos_file, todos)

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

            set_todos(todos_file, todos)
        case 4:
            # Complete operation
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)

            set_todos(todos_file, todos)
        case 5:
            # Exit operation
            break
        case _:
            print("Please input 1-5.")

print("\nGoodbye!\n")