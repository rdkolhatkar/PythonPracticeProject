# To run the "TutorialTen.py" file use command: python src/code/basics/10_TutorialTen.py
# Strings in Python
# This script demonstrates how to work with strings in Python.
name = "John Doe" # String with double quotes
print("The value of variable 'name' is:", name) # Output: The value of variable 'name' is: John Doe
print("The type of variable 'name' is:", type(name)) # Output: The type of variable 'name' is: <class 'str'>
name_single = 'Jane Doe' # String with single quotes
print("The value of variable 'name_single' is:", name_single) # Output: The value of variable 'name_single' is: Jane Doe
print("The type of variable 'name_single' is:", type(name_single)) # Output: The type of variable 'name_single' is: <class 'str'>
# Multiline strings using triple quotes
multiline_string = """This is a multiline string.
It can span multiple lines.
You can use triple quotes for this purpose."""
print("The value of variable 'multiline_string' is:\n", multiline_string) # Output: The value of variable 'multiline_string' is:
print("The type of variable 'multiline_string' is:", type(multiline_string)) # Output: The type of variable 'multiline_string' is: <class 'str'>
# Indexing and slicing strings
person = "Alice Wonderland"
first_char = person[0]    # First character of the string
print("The first character of 'person' is:", first_char) # Output: The first character of 'person' is: A
last_char = person[-1]  # Last character of the string
print("The last character of 'person' is:", last_char) # Output: The last character of 'person' is: d
substring = person[0:4]  # Slicing the first four characters
print("The first four characters of 'person' are:", substring) # Output: The first four characters of 'person' are: Alice
# Slicing the last four characters
last_four = person[-4:]     
print("The last four characters of 'person' are:", last_four) # Output: The last four characters of 'person' are: land
# String concatenation
greeting = "Hello, " + name + "!"   # Concatenating strings
print("The greeting message is:", greeting)    # Output: The greeting message is: Hello, John Doe!  
# String methods
uppercase_name = name.upper() # Convert to uppercase
print("The name in uppercase is:", uppercase_name) # Output: The name in uppercase is: JOHN DOE
lowercase_name = name.lower() # Convert to lowercase
print("The name in lowercase is:", lowercase_name) # Output: The name in lowercase is: john doe
title_name = name.title() # Convert to title case
print("The name in title case is:", title_name)   # Output: The name in title case is: John Doe       
# Checking if a string contains a substring
contains_alice = "Alice" in person      
print("Does 'person' contain 'Alice'? :", contains_alice) # Output: Does 'person' contain 'Alice'? : True
# Replacing a substring in a string
replaced_string = person.replace("Wonderland", "City") # Replace 'Wonderland' with 'City'
print("The string after replacement is:", replaced_string) # Output: The string after replacement is: Alice City
# String formatting
age = 30    # Example age variable
formatted_string = f"{name} is {age} years old."  # Using f-string for formatting
print("Formatted string:", formatted_string) # Output: Formatted string: John Doe is 30 years old.
# String length
string_length = len(person) # Get the length of the string
print("The length of 'person' is:", string_length)   # Output: The length of 'person' is: 16
# Checking if a string starts or ends with a specific substring
starts_with_alice = person.startswith("Alice") 
print("Does 'person' start with 'Alice'? :", starts_with_alice) # Output: Does 'person' start with 'Alice'? : True
ends_with_wonderland = person.endswith("Wonderland")
print("Does 'person' end with 'Wonderland'? :", ends_with_wonderland) # Output: Does 'person' end with 'Wonderland'? : True
# Splitting and joining strings
words = person.split()
print("The words in 'person' are:", words)  # Split the string into a list of words # Output: The words in 'person' are: ['Alice', 'Wonderland']
joined_string = " ".join(words) # Join the list of words back into a string # Output: The joined string is: Alice Wonderland
print("The joined string is:", joined_string) # Output: The joined string is: Alice Wonderland

