print("\nHi! Welcome to Todo List App\n")

file = open('todos.txt', 'r')
todos = file.readlines()
file.close()

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item[:-1]}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a todo: ")
            todos[number] = new_todo

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            number = number - 1
            todos.pop(number)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'exit':
            break

print("\nGoodbye!\n")