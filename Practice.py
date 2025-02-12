# Python program for beginners

# Data types and variables
integer_var = 10
float_var = 20.5
string_var = "Hello, World!"
boolean_var = True

print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)

# Lists
fruits = ["Apple", "Banana", "Cherry"]
print("\nList of fruits:", fruits)
print("First fruit:", fruits[0])

# Adding an element to the list
fruits.append("Date")
print("List of fruits after adding an element:", fruits)

# Removing an element from the list
fruits.remove("Banana")
print("List of fruits after removing an element:", fruits)

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("\nDictionary:", person)
print("Name:", person["name"])

# Adding a new key-value pair
person["email"] = "john@example.com"
print("Dictionary after adding a key-value pair:", person)

# Removing a key-value pair
del person["age"]
print("Dictionary after removing a key-value pair:", person)

# Loops
print("\nFor loop example:")
for fruit in fruits:
    print(fruit)

print("\nWhile loop example:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print("\nFunction example:")
print(greet("Alice"))

# File handling
print("\nFile handling example:")
file_path = "example.txt"

# Writing to a file
with open(file_path, "w") as file:
    file.write("This is an example file.\n")
    file.write("Hello, World!\n")

# Reading from a file
with open(file_path, "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("\nException handling example:")
    print("Error: Division by zero is not allowed.")

# End of the beginner practice program


