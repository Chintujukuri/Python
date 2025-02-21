"""
Python List - Complete Guide

A list is an ordered, mutable collection that allows duplicate values.
"""

# 1️⃣ Creating a List
numbers = [10, 20, 30, 40, 50]  # List of integers
fruits = ["apple", "banana", "cherry"]  # List of strings
mixed = [10, "hello", 3.14, True]  # Mixed data types
empty_list = []  # Empty list

# 2️⃣ Accessing List Elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1]) # Output: cherry (last element)

# 3️⃣ Modifying a List
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']

# 4️⃣ List Methods
numbers.append(60)   # Adds an item
numbers.insert(2, 25) # Inserts at index 2
numbers.remove(40)   # Removes first occurrence
print(numbers)

# 5️⃣ Looping Through a List
for fruit in fruits:
    print(fruit)

# 6️⃣ List Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# 7️⃣ Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6

# 8️⃣ Copying a List
new_fruits = fruits.copy()
new_fruits.append("grape")
print(new_fruits)

# 9️⃣ Checking if an Element Exists
if "banana" in fruits:
    print("Banana is in the list")

# 🔟 Deleting Elements
del numbers[2]
numbers.remove(60)
print(numbers)
