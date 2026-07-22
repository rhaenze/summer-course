# #Hands on Lesson 4
#  IS ON my Reading_errors directory


# # Python will show you exactly what is wrong with the carrots point to the issue




# #1 

# def greet(name):
#     message = "Hello, " + name
#     print(mesage)

# greet("Alice")


# # CORRECTED CODE:
# # 'Message' is spelt wrong in line 14


# def greet(name):
#     message = "Hello, " + name
#     print(message)

# greet("Alice")

# #RAN CORRECTLY 



# Exercise 2: SyntaxError - Missing Punctuation
# Goal: Learn to identify and fix syntax errors.

# # Create syntax_errors.py:


# def calculate_total(price, quantity):
#     total = price * quantity
#     print(f"Total: {total"
#     return total

# calculate_total(10, 5)


# CORRECTED CODE:
# 'Total' in line 41 needs to be 'total'. Captilization matters!!!!
# You need to close the total } and add a ) at the end in line 52



# def calculate_total(price, quantity):
#     total = price * quantity
#     print(f"total: {total}")
#     return total

# calculate_total(10, 5)


#CODE RAN CORRECTLY


# # #2 Part two 

# def greet(name):
#     print(f"Hello, {name}")

# greet("Bob")



# #CORRECTED CODE:
# # Needed a : after the parenethesis on line 66

# # CODE RUNS CORRECTLY 



# Exercise 3: NameError - Undefined Variables
# Goal: Understand NameError and when it occurs.


# print(user_name)
# user_name = "Charlie"


#Correction to code
# The order is out of order. You are printing nothing that is defined. Python reads like a book, top down!!!!

#CORRECTED CODE:

user_name = "Charlie"
print(user_name)