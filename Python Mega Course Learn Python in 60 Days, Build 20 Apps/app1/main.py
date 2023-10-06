user_prompt = "Enter a todo:"

while True:
    user_input = input(user_prompt)
    if user_input == "quit":
        break
    else:
        print(user_input)