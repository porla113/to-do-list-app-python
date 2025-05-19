import FreeSimpleGUI as sg
import functions
import time

# File path
todos_file = 'todos.txt'

# Window
# Window's contents
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(todos_file), 
                      key='todos', enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")

layout = [[sg.Text("Type in a to-do")],
          [input_box, add_button],
          [list_box, edit_button]]

font = ('Helvetica', 15)
# Create the window
window = sg.Window('To-Do App', layout, font=font)
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            # Add operation
            todos = functions.get_todos(todos_file)
            todo = values['todo'].replace('\n','') + "\n"
            todos.append(todo)

            functions.write_todos(todos_file, todos)

            # Update list box
            window['todos'].update(values=todos)

        case "Edit":
            to_edit = values['todos'][0]
            new_todo = values['todo'].replace('\n','') + "\n"

            todos = functions.get_todos(todos_file)
            index_to_edit = todos.index(to_edit)
            todos[index_to_edit] = new_todo

            functions.write_todos(todos_file, todos)

            # Update list box
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])
            
        case sg.WIN_CLOSED:
            break
window.close()


# Menu
optMenu = """
========== Operation ===========
1. Add          4. Complete
2. Show         5. Exit
3. Edit
"""

'''
# Greeting message
print("\nHi! Welcome to Todo List App\n")

# Create todos list from a text file
todos = functions.get_todos(todos_file)

while True:
    now = time.strftime("%d %b %Y, %H:%M:%S")
    print(f"It is {now}.")
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
'''