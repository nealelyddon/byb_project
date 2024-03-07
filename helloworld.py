# Input validation function
def validate_name(name): # Checks if the input contains only alphabetic characters
    if name.isalpha() or ' ' in name:
        return True
    else:
        return False

# Prompt user for a valid name
user_input = input("Please enter your name: ")
while not validate_name(user_input): # Script repeatedly prompts the user until a valid name is entered
    print("Invalid input. Please enter a valid name.")
    user_input = input("Please enter your name: ")

# Greet the user
print("Hello! " + user_input)
