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



