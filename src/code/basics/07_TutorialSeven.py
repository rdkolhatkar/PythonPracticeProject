# To run the "TutorialSeven.py" file use command: python src/code/basics/07_TutorialSeven.py
# Match Case Statements in Python
print("Welcome to the Match Case tutorial!")
# It was introduced in Python 3.10.
# Match case is a powerful feature that allows you to match patterns in data structures.
# It is similar to switch-case statements in other programming languages.
# Here is an example of how to use match case statements:
status = "active"
match status:
    case "active":  # If status is "active"
        print("The user is active.")
    case "inactive":  # If status is "inactive"
        print("The user is inactive.")
    case "banned":  # If status is "banned"
        print("The user is banned.")
    case _:  # Default case if none of the above match
        print("Unknown status.")

number = int(input("Enter a number (1- 100): "))
match number % 2:
    case 0:  # If number is even (remainder is 0)
        print(f"{number} is an even number.")
    case 1:  # If number is odd (remainder is 1)
        print(f"{number} is an odd number.")
    case _:  # Default case if number is not in the range
        print("Number is out of range. Please enter a number between 1 and 100.")

# Match case can also be used with complex data structures like lists and dictionaries.
user = {"name": "Alice", "age": 30, "status": "active"}
match user:
    case {"name": name, "age": age, "status": "active"}:    # If user has name, age, and status as active
        print(f"{name} is an active user, age {age}.")
    case {"name": name, "age": age, "status": "inactive"}:  # If user has name, age, and status as inactive
        print(f"{name} is an inactive user, age {age}.")
    case _:
        print("User data does not match any known pattern.")  
