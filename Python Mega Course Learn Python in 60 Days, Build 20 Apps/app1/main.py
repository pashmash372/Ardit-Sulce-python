todos = []

while True:
    user_action = input("Type add , show , edit or exit: ")

    match user_action.strip():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for todo in todos:
                todo = todo.title()
                print(todo)
        case "exit":
            break
        case "edit":
            number= input("Number of the todo to edit: ")
            existing_todo = todos[int(number) - 1] # int converts string to number
            new_todo = input("New todo: ")
            todos[int(number) - 1] = new_todo
        case _:
            print("Invalid action")
print("Bye!")
