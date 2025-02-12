import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Creating a 2D spiral spring plot
theta = np.linspace(0, 4 * np.pi, 100)
z = np.linspace(0, 1, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

plt.figure()
plt.plot(x, y)
plt.title("2D Spiral Spring")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("2D_spiral_spring.png")
plt.show()

# Creating a 3D spiral spring plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_title("3D Spiral Spring")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_spiral_spring.png")
plt.show()

# Creating a 3D surface plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_title("3D Surface Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.savefig("3D_surface_plot.png")
plt.show()

# End of the beginner and advanced practice program
