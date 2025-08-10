# To run the "TutorialFour.py" file use command: python src/code/basics/04_TutorialFour.py
# Comments in python start with a hash symbol
# This is a single-line comment
# This is a multi-line comment
"""
This is a multi-line comment
that spans multiple lines.
"""
# This is another multi-line comment
'''
This is also a multi-line comment
that can be used to explain code in detail.
'''
# Escape sequences characters
print("Hello, How are you!")  # This prints a message to the console
# We cannot terminate a string literal in next line
# Now to write a string in multiple lines we can use \n
print("Hello, \nHow are you!")  # This prints a message with a newline character
# We can also use triple quotes to write multi-line strings
print("""Hello,
How are you!""")  # This prints a message with a newline character using triple quotes
# Below are the list of escape sequences characters
# \n - Newline -> Moves the cursor to the next line
# \t - Tab -> Inserts a tab space
# \\ - Backslash -> Inserts a backslash character
# \r - Carriage return -> Moves the cursor to the beginning of the line
# \b - Backspace -> Moves the cursor one character back
# \f - Form feed -> Moves the cursor to the next page
# \a - Bell/Alert -> Triggers a sound alert
# \v - Vertical tab -> Moves the cursor down to the next vertical tab stop
# \0 - Null character -> Represents a null character
# \' - Single quote -> Inserts a single quote character
# \" - Double quote -> Inserts a double quote character

# Features of Print function
# Print function is used to print the output to the console
# Print function can be written using single quotes or double quotes
print('Hello, World!')  # This prints a message using single quotes
print("Hello, World!")  # This prints a message using double quotes
# Print function can take multiple arguments
print("Hello", "World", "from", "Python!")
print("Hello World \" from Python!")  # This prints a message with a newline character
# Print function can take keyword arguments
print("Hello", "World", sep=", ", end="!\n")  # This prints a message with a custom separator and end character
# Print function is by default gie you a newline character at the end
# To override this default behavior, we can use the "end" keyword argument
print("Hello, World!", end="")  # This prints a message without a newline at the end
print("How are you?")
#  "sep" keyword argument is used to specify the separator between the arguments -> default is a space
print("Hello", "World", end=" ", sep=" ")  
print("How are you doing?")
print("Hello World", sep=" _ ")  # This prints a message with a custom separator
print("How are you doing?")
print("Hello World", "Is it working?", sep=" _ ")
print("Yes, it is working!", end=" :)")  # This prints a message with a custom end character because of the "end" keyword argument
