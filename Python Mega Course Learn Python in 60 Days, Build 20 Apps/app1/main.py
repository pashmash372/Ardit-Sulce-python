user_prompt = "Enter a todo:"
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print(todos)
print(type(user_prompt))  # <class 'str'>
print(type(todos))  # <class 'list'>

# when to use single quotes vs double quotes ?
# single quotes are used for strings that contain double quotes
# double quotes are used for strings that contain single quotes
# triple quotes are used for strings that contain both single and double quotes

# example of single quotes
print('I said, "Hello" to you.')
# example of double quotes
print("I said, 'Hello' to you.")
# example of triple quotes
print('''I said, "Hello" to you.''')
print("""I said, 'Hello' to you.""")
print('''I said, "Hello" to you.''')

#  which is better to use single quotes or double quotes ?
# it doesn't matter, just be consistent
