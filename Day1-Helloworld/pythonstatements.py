#python statement :- A statement is a single instruction that Python can execute print("Hello")
#types

"""
DAY 1: Python Statements and Their Real-World Uses
"""
# -----------------------------
# 1. Assignment Statements
# -----------------------------
# Used to store data in variables.

price = 500
discount = 50
final_price = price - discount   # Real-world: billing system

print("Final Price after discount:", final_price)
#result final_price = 450


# -----------------------------
# 2. Expression Statements
# -----------------------------
# Performs calculations or operations.

total_marks = 80 + 15  # Real-world: Student score calculation
print("Total Marks:", total_marks)


# -----------------------------
# 3. Print Statement
# -----------------------------
# Displays output to user.

print("Welcome to Python!")  # Real-world: Display messages/logs


# -----------------------------
# 4. Conditional Statements
# -----------------------------
# Used for decision making.

age = 20
if age >= 18:
    print("User is an adult")  # Real-world: Age verification
else:
    print("User is a minor")


# -----------------------------
# 5. Loop Statements
# -----------------------------
# Used to repeat a block of code.

items = ["Apple", "Banana", "Orange"]
for item in items:
    print("Item:", item)  # Real-world: Processing list of items


# -----------------------------
# 6. Input Statement
# -----------------------------
# Takes user input. (Commented to avoid stopping execution)

# name = input("Enter your name: ")  # Real-world: Login or sign-up
# print("Hello,", name)


# -----------------------------
# 7. Import Statement
# -----------------------------
# Used to load external modules.

import math
print("Square root of 25:", math.sqrt(25))  # Real-world: Calculations


# -----------------------------
# 8. Function Definition + Return Statements
# -----------------------------
# Used for reusable code blocks.

def add(a, b):
    return a + b  # Real-world: Common utility function

print("Sum:", add(10, 20))


# -----------------------------
# 9. Pass Statement
# -----------------------------
# Placeholder when code is not ready yet.

def future_feature():
    pass  # Real-world: Planning structure for future features
