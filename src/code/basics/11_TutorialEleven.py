# To run the the ""TutorialEleven.py" file use command :  python src/code/basics/11_TutorialEleven.py
# String Methods in Python & String Formatting Manipulation
print("Welcome to Tutorial Eleven!")
name = "Harry0123456789"
print(name[0:2]) # goes from 0 to 2-1 ie 0 to 1
print(name[2:-1]) # Same as name[2:4]
print(name[0:10:4]) # Skip n- 1 characters
print(name[0:10:1]) # Skip 0 character
print(name[0:10:3]) # Skip 3-1 ie 2 characters
print(name[:4]) # Replace the first empty number with 0 # name[0:4]
print(name[1:]) # Replace the second empty number with length # name[1:15]
# String manipulation and formatting
# Slicing a string
sample_string = "HelloWorld!!"
print("Sample String Length:", len(sample_string))  # Length of the string 
print("Original String:", sample_string)
print("Sliced String (0 to 5):", sample_string[0:5])  # Slicing from index 0 to 5 goes from index 0 to 5-1 i.e 0 to 4
print("Sliced String (7 to end):", sample_string[7:]) 
# Slicing based on positive and negative indices
print("Sliced String (-6 to end):", sample_string[-6:])
print("Sliced String (0 to -7):", sample_string[0:-7]) # same as sample_string[0:len(sample_string)-7] i.e 0 to 6
print("Sliced String (2 to -1):", sample_string[2:-1])  
value = "Alice1234567890"
print(value[0:5:2]) 
print(value[::2]) 
print(value[0:10:3]) 
# String methods
print("Uppercase:", sample_string.upper())  # Convert to uppercase
print("Lowercase:", sample_string.lower())  # Convert to lowercase
print("Title Case:", sample_string.title())  # Convert to title case
print("Reversed String:", sample_string[::-1])  # Reverse the string
print("Count of 'o':", sample_string.count('o'))  # Count occurrences of 'o'
print("Index of 'W':", sample_string.index('W'))  # Find index of 'W'
print("Replace 'Hello' with 'Hi':", sample_string.replace('Hello', 'Hi'))
# String formatting
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted String:", formatted_string)
# Removing whitespace
whitespace_string = "   Hello World!   "
print("Original String with Whitespace:", repr(whitespace_string))
print("String after stripping whitespace:", whitespace_string.strip())  
# Checking if a string starts or ends with a specific substring
print("Starts with 'Hello':", sample_string.startswith('Hello'))    
print("Ends with '!!':", sample_string.endswith('!!'))
# Checking if a string contains only digits or alphabetic characters
print("Contains only digits:", value.isdigit())  # Check if all characters are digits
s = "hello world" # Strings are immutable

# s[0] = "R" # You cannot do this

a = len(s)
print(a)
print(s.upper(), s)
print(s.lower())
print(s.capitalize())
print(s.title())

text = " \nhello world "
print(text.strip()) # Output: "hello world"
print(text.lstrip()) # Output: "hello world "
print(text.rstrip()) # Output: " hello world"


text = "Python is fun and fun and fun"
print(text.find("is")) # Output: 7 Index of first occurence
print(text.replace("fun", "awesome")) 


text = "Apples,Bananas,Pineapples"
print(text.split(","))
print(",".join(['Apples', 'Bananas', 'Pineapples']))

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False