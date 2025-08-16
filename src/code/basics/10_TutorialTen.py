# To run the "TutorialTen.py" file use command: python src/code/basics/10_TutorialTen.py
# Strings in Python
# This script demonstrates how to work with strings in Python.
name = "John Doe" # String with double quotes
print("The value of variable 'name' is:", name)
print("The type of variable 'name' is:", type(name))
name_single = 'Jane Doe' # String with single quotes
print("The value of variable 'name_single' is:", name_single)
print("The type of variable 'name_single' is:", type(name_single))
# Multiline strings using triple quotes
multiline_string = """This is a multiline string.
It can span multiple lines.
You can use triple quotes for this purpose."""
print("The value of variable 'multiline_string' is:\n", multiline_string)
print("The type of variable 'multiline_string' is:", type(multiline_string))
# Indexing and slicing strings
person = "Alice Wonderland"
first_char = person[0]    # First character of the string
print("The first character of 'person' is:", first_char)
last_char = person[-1]  # Last character of the string
print("The last character of 'person' is:", last_char)
substring = person[0:4]  # Slicing the first four characters
print("The first four characters of 'person' are:", substring)
# Slicing the last four characters
last_four = person[-4:]     
print("The last four characters of 'person' are:", last_four)
# String concatenation
greeting = "Hello, " + name + "!"   # Concatenating strings
print("The greeting message is:", greeting)     
# String methods
uppercase_name = name.upper() # Convert to uppercase
print("The name in uppercase is:", uppercase_name)
lowercase_name = name.lower() # Convert to lowercase
print("The name in lowercase is:", lowercase_name)
title_name = name.title() # Convert to title case
print("The name in title case is:", title_name)         
# Checking if a string contains a substring
contains_alice = "Alice" in person      
print("Does 'person' contain 'Alice'? :", contains_alice)
# Replacing a substring in a string
replaced_string = person.replace("Wonderland", "City") # Replace 'Wonderland' with 'City'
print("The string after replacement is:", replaced_string)
# String formatting
age = 30    # Example age variable
formatted_string = f"{name} is {age} years old."  # Using f-string for formatting
print("Formatted string:", formatted_string)
# String length
string_length = len(person) # Get the length of the string
print("The length of 'person' is:", string_length)  
# Checking if a string starts or ends with a specific substring
starts_with_alice = person.startswith("Alice")
print("Does 'person' start with 'Alice'? :", starts_with_alice)
ends_with_wonderland = person.endswith("Wonderland")
print("Does 'person' end with 'Wonderland'? :", ends_with_wonderland)
# Splitting and joining strings
words = person.split()
print("The words in 'person' are:", words)  # Split the string into a list of words
joined_string = " ".join(words) # Join the list of words back into a string
print("The joined string is:", joined_string)

