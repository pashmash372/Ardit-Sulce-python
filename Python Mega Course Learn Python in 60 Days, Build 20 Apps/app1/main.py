todos = []

while True:
    user_action = input("Type add , show or exit: ")

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
        case _:
            print("Invalid action")
print("Bye!")
