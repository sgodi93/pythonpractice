# This file is created to list the operations that can be performed on a given string with it's available methods

print("Python string operations")

a = input("Please Enter a string: ")

print(f"The total no. of operations that can be performed on the given string are ", len(dir(a)))

print(f"The available properties and methods for the given string {a} are: ", dir(a))

print(f"The capitalized version of {a} is, ", a.capitalize())

print(f"The version of the string suitable for caseless comparision is ", a.casefold())

print(f"To print {a} in center or with given indentation or characters")

print(a.center(50))
print(a.center(60, "$"))

b = input("Please enter a substring/char to return the no.of occurences: ")

print(f"The no. of non-overlapping occurences of the given substring sub {b} in string {a}, ", a.count(b))

print(f" Encoded output of {a} is ", a.encode())

c = input("Please enter a suffix : ")

print(f"Checking whether the string '{a}' endswith the given suffix '{c}' by returning True/False:  ", a.endswith(c))

print(f"Returnig a copy where all tab characters are expanded using spaces: ", a.expandtabs())

d = input("Please enter a character to find its lowest index if find from main string : ")

print(f"The lowest index of '{d}' in the given input string '{a}' is : ", a.find(d))

e = input("Please enter a character present in string to find its index : ")

print(f"The lowest index of '{e}'  if found from the string '{a}' is : ", a.index(e))

print("Checking format methods.........")
name = input("Please enter your name: ")
age = input("Please enter your age: ")

print("Hi all, this is {n}, and i am {a} years old".format(n= name, a= age))

# format_map method can be used when we want to print some data using some input dictionary
data = {"name": "Surya", "age": 30, "city": "Cincinnati"}

print("Hello, My name is {name}, I am {age} years old and I live in {city}".format_map(data))

# String Checking Methods
print("String checking methods and returns bool value")

print(f" Checks if all characters are alphabets of given string {a}", a.isalpha())

print(f"Checks if all characters are digits of given string '{a}'", a.isdigit())

print(f"Checks if all characters are alphanumeric(letters & numbers) of given string '{a}'", a.isalnum())

print(f"Checks if a given string '{a}' contains only spaces ", a.isspace())

print(f"Checks if all characters in given string '{a}' are lowercase : ", a.islower())

print(f"Checks if all characters in given string '{a}' are uppercase : ", a.isupper())

print(f"Checks if the given string is in title case :", a.istitle())

print(f" Checks if the given string is decimal or not : ", a.isdecimal())

print(f" Checks is the given string is numeric or not : ", a.isnumeric())

# Return True or False -- isidentifier
# Returns True -- "string"
# Returns False -- "789786Hghj%$%^8"

print(f"Checks whether given string '{a}' is valid Python identifier or not by returning True/False: ", a.isidentifier())

print(f"Checks the input string printable or not : ", a.isprintable())

string1 = input("Please enter a string: ")
string2 = input("Please enter a random string: ")

print(f" To join {string1} and {string2} :", "".join([string1, string2]))

print(f" Returns a left-justified string of length width and padding is done using the specified fill character : ", a.ljust(30, '$'))

print(f"Returns the lower case of the given string : ", a.lower())

str_wit_spaces = "       Hello       "

print(f"Returns a copy of the string with leading white spaces removed : ", str_wit_spaces.lstrip())

print(f"Returns a copy of the string with trainling white spaces removed : ", str_wit_spaces.rstrip())

print(f"Returns a copy of the string with leading and trainling white spaces removed : ", str_wit_spaces.strip())

# maketrans and translate method

# Basic Character mapping

# Create translation table
trans_table = str.maketrans("aeiou", "12345")

# Apply translation
result = "hello world".translate(trans_table)

print(result)  # h2ll4 w4rld

# Removing Specific Characters

# Remove vowels from the string
trans_table = str.maketrans("", "", "aeiou")
result = "hello world".translate(trans_table)

print(result)  # hll wrld

# The .partition() method is used to split a string into three parts based on the first occurrence of a specified separator. It returns a tuple 

s = "hello-world-python"
result = s.partition("-")

print(result)  # ('hello', '-', 'world-python')

# If you want to split from the last occurrence of a separator, use .rpartition()

s = "apple-orange-banana"
result = s.rpartition("-")

print(result)  # ('apple-orange', '-', 'banana')

# removeprefix() and removesuffix()

s = "PythonProgramming"
print(s.removeprefix("Python"))  # Output: 'Programming'

# If prefix is not found, the string remains unchanged
print(s.removeprefix("Java"))    # Output: 'PythonProgramming'

s = "data_backup.zip"
print(s.removesuffix(".zip"))  # Output: 'data_backup'

# If suffix is not found, the string remains unchanged
print(s.removesuffix(".tar"))  # Output: 'data_backup.zip'

filename = "report_final.pdf"

# Remove .pdf extension
new_filename = filename.removesuffix(".pdf")

print(new_filename)  # Output: 'report_final'

# The replace() method in Python is used to replace occurrences of a substring within a string with another substring

text = "Hello, World!"
new_text = text.replace("World", "")

print(new_text)  
# Output: "Hello, !"

# startswith() – Checks if a String Starts with a Specific Prefix

text = "Python is fun"

print(text.startswith("Python"))  # True
print(text.startswith("Java"))    # False
print(text.startswith("Py"))      # True
print(text.startswith("is", 7))   # True (Starts checking from index 7)

# swapcase() – Swaps Uppercase to Lowercase and Vice Versa

text = "Hello World"

print(text.swapcase())  # "hELLO wORLD"
print("PyThOn".swapcase())  # "pYtHoN"

# zfill() – Pads a String with Zeros on the Left

text = "42"

print(text.zfill(5))  # "00042"
print("123".zfill(6))  # "000123"


