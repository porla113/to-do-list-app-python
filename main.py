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
    Read a text file and return a list of to-do items
    Arguments:
    - filepath - string
    Return:
    - a list of string
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

# write_todos function
def write_todos(filepath, todos_list):
    """
    Write a list of to-do items to a text file
    Arguments:
    - filepath: string
    - todos_list: a list of string
    Return:
    - None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)

# check_int_input function
def isValid_intInput(input, start, stop):
    """
    Check that input string is integer and it is between start and stop
    Arguments:
    - input: string
    - start: int
    - stop: int
    Return:
    - True: input string is an integer and its value is between start and stop arguments
    - False: otherwise
    """
    try:
        intInput = int(input)
    except ValueError:
        return False

    if intInput >= start and intInput <= stop:
            return True 
    else:
        return False

# Greeting message
print("\nHi! Welcome to Todo List App\n")

# Create todos list from a text file
todos = get_todos(todos_file)

while True:
    # Main menu loop
    while True:
        print(optMenu)
        user_action = input("Select an operation with number 1-5: ")
        if isValid_intInput(user_action,1,5):
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

            write_todos(todos_file, todos)

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

            write_todos(todos_file, todos)
        case 4:
            # Complete operation
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)

            write_todos(todos_file, todos)
        case 5:
            # Exit operation
            break
        case _:
            print("Please input 1-5.")

print("\nGoodbye!\n")