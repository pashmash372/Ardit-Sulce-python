todos = []

while True:
    user_action = input("Type add , show or exit: ")

    match user_action.strip():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for todo in todos:
                print(todo)
        case "exit":
            break

print("Bye!")
