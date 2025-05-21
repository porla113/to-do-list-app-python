import FreeSimpleGUI as sg
import functions
import time

# File path
todos_file = 'todos.txt'

# Window
# Theme
sg.theme('BrownBlue')
# Window's contents
text_time = sg.Text("", key="clock")
text_instruct = sg.Text("Type in a to-do")
text_to_user = sg.Text(text_color="black", key="text_to_user")
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(todos_file), 
                      key='todos', enable_events=True,
                      size=[45, 10])

layout = [[text_time], 
          [text_instruct],
          [text_to_user],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

font = ('Helvetica', 15)

# Create the window
window = sg.Window('To-Do App', layout, font=font)

while True:
    event, values = window.read(timeout=200)

    if event in (None, 'exit', sg.WIN_CLOSED):
        break

    if values is not None:
        window['clock'].update(value=time.strftime("%d %b %Y, %H:%M:%S"))
        
        # Debug
        # print(event)
        # print(values)

        match event:
            case "Add":
                # Add operation
                if len(values['todo']) == 0:
                    window['text_to_user'].update(value="!!! Please type a todo.")
                else:
                    todos = functions.get_todos(todos_file)
                    todo = values['todo'].replace('\n','') + "\n"
                    todos.append(todo)

                    functions.write_todos(todos_file, todos)

                    # Update list box
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')

            case "Edit":
                try:
                    to_edit = values['todos'][0]
                    new_todo = values['todo'].replace('\n','') + "\n"

                    todos = functions.get_todos(todos_file)
                    index_to_edit = todos.index(to_edit)
                    todos[index_to_edit] = new_todo

                    functions.write_todos(todos_file, todos)

                    # Update list box
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
                except IndexError:
                    sg.popup("!!! Please select a todo to edit.", title="Oops!", font=("Helvetica", 15))

            case "Complete":
                try:
                    to_complete = values['todos'][0]

                    todos = functions.get_todos(todos_file)
                    todos.remove(to_complete)

                    functions.write_todos(todos_file, todos)

                    # Update list box
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
                except IndexError:
                    sg.popup("!!! Please select a todo to complete.", title="Oops!", font=("Helvetica", 15))

            case "todos":
                window['todo'].update(value=values['todos'][0])

            case "Exit":
                break
                
            case sg.WIN_CLOSED:
                break

window.close()