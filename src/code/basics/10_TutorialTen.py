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
substringNew = person[:4] # Slicing the first four characters using shorthand notation
print("The first four characters of 'person' using shorthand notation are:", substringNew) # Output: The first four characters of 'person' using shorthand notation are: Alic
# Here in above case the start index is omitted, so it defaults to 0, which is the beginning of the string. And the end index is 4, which means it will slice up to but not including the character at index 4.
# Negative indexing allows you to slice from the end of the string. Here we are slicing the last four characters of the string. 
negative_slice = person[-4:-1] # Slicing the last four characters except the last one
print("The last four characters of 'person' except the last one are:", negative_slice) # Output: The last four characters of 'person' except the last one are: land
# In the above case, the start index is -4, which means it starts slicing from the fourth character from the end of the string. The end index is -1, which means it slices up to but not including the last character of the string. So it will slice the characters at indices -4, -3, and -2, which are 'l', 'a', and 'n' respectively.
# In simple words : person[-4, -1] is equa to person[len(person)-4 : len(person)-1]
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
# Removing Trailing Characters
string_with_specialChars = "&&&& Hello, World! &&&&&&" # String with leading and trailing whitespace and special characters
stripped_string = string_with_specialChars.rstrip('&') # Remove trailing special characters, It does not remove leading special characters, so the leading '&&&& ' will remain unchanged. The rstrip() method only removes characters from the end of the string, not from the beginning.
print("The stripped string is:", stripped_string) # Output: The stripped string is: &&&& Hello, World!
stripped_string_leading = string_with_specialChars.lstrip('&') # Remove leading special characters, It does not remove trailing special characters, so the trailing ' &&&&&&' will remain unchanged. The lstrip() method only removes characters from the beginning of the string, not from the end.
print("The stripped string with leading characters removed is:", stripped_string_leading) # Output: The stripped string with leading characters removed is:  Hello, World! &&&&&&
stripped_string_both = string_with_specialChars.strip('&') # Remove both leading and trailing special characters, It removes both leading and trailing '&&&& ' and ' &&&&&&' from the string. The strip() method removes characters from both the beginning and the end of the string.
print("The stripped string with both leading and trailing characters removed is:", stripped_string_both) # Output: The stripped string with both leading and trailing characters removed is:  Hello, World!
# Removing whitespace
string_with_whitespace = "   Hello, World!   " # String with leading and trailing whitespace
stripped_whitespace = string_with_whitespace.strip() # Remove leading and trailing whitespace   
print("The string with whitespace removed is:", stripped_whitespace) # Output: The string with whitespace removed is: Hello, World!
# In the above case, the strip() method removes all leading and trailing whitespace characters from the string. So the resulting string will be "Hello, World!" without any extra spaces at the beginning or end.
# Capitalize the first letter of each word in a string
heading = "the quick brown fox jumps over the lazy dog" # Capitalize the first letter of each word in the string
capitalized_string = heading.capitalize() # The capitalize() method capitalizes only the first character of the string and converts the rest of the characters to lowercase. So the resulting string will be "The quick brown fox jumps over the lazy dog" with only the first letter 'T' capitalized and the rest of the letters in lowercase.
print("The capitalized string is:", capitalized_string) # Output: The capitalized string is: The quick brown fox jumps over the lazy dog
# center() method centers the string within a specified width by padding it with spaces on both sides. If the specified width is greater than the length of the string, it will add spaces to the left and right of the string to center it. If the specified width is less than or equal to the length of the string, it will return the original string without any changes.
centered_string = heading.center(50) # Center the string within a width of 50   
print("The centered string is:\n", centered_string) # Output: The centered string is: the quick brown fox jumps over the lazy dog
print("The length of the centered string is:", len(centered_string)) # Output: The length of the centered string is: 50
# count() method counts the number of occurrences of a substring in a string. It takes the substring as an argument and returns the number of times it appears in the string. If the substring is not found, it returns 0.
count_the = heading.count("the") # Count the number of occurrences of "the" in the string
print("The number of occurrences of 'the' in the string is:", count_the) # Output: The number of occurrences of 'the' in the string is: 2
count_fox = heading.count("fox") # Count the number of occurrences of "fox" in the string
print("The number of occurrences of 'fox' in the string is:", count_fox) # Output: The number of occurrences of 'fox' in the string is: 1
count_cat = heading.count("cat") # Count the number of occurrences of "cat" in the string
print("The number of occurrences of 'cat' in the string is:", count_cat) # Output: The number of occurrences of 'cat' in the string is: 0
# endswith() method checks if a string ends with a specified substring. It takes the substring as an argument and returns True if the string ends with that substring, and False otherwise.
ends_with_dog = heading.endswith("dog") # Check if the string ends with "dog"
print("Does the string end with 'dog'? :", ends_with_dog) # Output: Does the string end with 'dog'? : True
ends_with_cat = heading.endswith("cat") # Check if the string ends with "cat"       
print("Does the string end with 'cat'? :", ends_with_cat) # Output: Does the string end with 'cat'? : False
print(heading.endswith("k bro", 8, 10)) # Check if the substring "k bro" is at the end of the string when considering only the characters from index 8 to 10. Output: False
print(heading.endswith("k bro", 8, 13)) # Check if the substring "k bro" is at the end of the string when considering only the characters from index 8 to 13. Output: True
# find() method searches for the first occurrence of a specified substring in a string and returns the index of the first character of the substring. If the substring is not found, it returns -1.
index_quick = heading.find("quick") # Find the index of the first occurrence of "quick" in the string
print("The index of the first occurrence of 'quick' is:", index_quick) # Output: The index of the first occurrence of 'quick' is: 4
index_cat = heading.find("cat") # Find the index of the first occurrence of "cat" in the string
print("The index of the first occurrence of 'cat' is:", index_cat) # Output: The index of the first occurrence of 'cat' is: -1  
# index() method is similar to find() but raises a ValueError if the substring is not found instead of returning -1.
try:
    index_cat_index = heading.index("cat") # Find the index of the first occurrence of "cat" in the string using index() method
    print("The index of the first occurrence of 'cat' using index() method is:", index_cat_index) # This line will not be executed because a ValueError will be raised      
except ValueError:
    print("The substring 'cat' was not found in the string using index() method.") # Output: The substring 'cat' was not found in the string using index() method.
    
# isalnum() method checks if all characters in the string are alphanumeric (letters and numbers) and there is at least one character. It returns True if the string is alphanumeric, and False otherwise.
alphanumeric_string = "Hello123" # String that is alphanumeric  
is_alphanumeric = alphanumeric_string.isalnum() # Check if the string is alphanumeric
print("Is the string 'Hello123' alphanumeric? :", is_alphanumeric) # Output: Is the string 'Hello123' alphanumeric? : True
non_alphanumeric_string = "Hello 123!" # String that is not alphanumeric due to the presence of a space and an exclamation mark
is_non_alphanumeric = non_alphanumeric_string.isalnum() # Check if the string is alphanumeric
print("Is the string 'Hello 123!' alphanumeric? :", is_non_alphanumeric) # Output: Is the string 'Hello 123!' alphanumeric? : False
empty_string = "" # An empty string is not considered alphanumeric because it does not contain any characters.
is_empty_alphanumeric = empty_string.isalnum() # Check if the empty string is alphanumeric
print("Is the empty string alphanumeric? :", is_empty_alphanumeric) # Output: Is the empty string alphanumeric? : False 
# isupper() and islower() methods check if all characters in the string are uppercase or lowercase letters, respectively. They return True if the condition is met, and False otherwise.
uppercase_string = "HELLO" # String that is in uppercase 
is_uppercase = uppercase_string.isupper() # Check if the string is in uppercase
print("Is the string 'HELLO' in uppercase? :", is_uppercase) # Output: Is the string 'HELLO' in uppercase? : True
lowercase_string = "hello" # String that is in lowercase
is_lowercase = lowercase_string.islower() # Check if the string is in lowercase
print("Is the string 'hello' in lowercase? :", is_lowercase) # Output: Is the string 'hello' in lowercase? : True
# swapcase() method returns a new string where all uppercase letters are converted to lowercase and all lowercase letters are converted to uppercase.
mixed_case_string = "Hello World!" # String with mixed case
swapped_case_string = mixed_case_string.swapcase() # Swap the case of each character in the string
print("The string with swapped case is:", swapped_case_string) # Output: The string with swapped case is: hELLO wORLD!
# missing string methods: isalpha(), isdigit(), isspace(), startswith(), endswith(), splitlines(), partition(), rpartition(), zfill(), expandtabs(), maketrans(), translate() etc. You can explore these methods in the Python documentation for strings to learn more about their functionality and usage.
