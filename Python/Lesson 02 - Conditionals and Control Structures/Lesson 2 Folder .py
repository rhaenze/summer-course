# Conditionals Statements
# The "IF" Statement
#     Syntax:
#     if condition
#         # Code to execute if condition is true
#     Example:
#         1. age=20
#         2. if age >= 18:
#             print("You are eligible to vote.")
# The Else Statement
#     Syntax:
#     if condition:
#         # Code to execute if condition is true
#     else:
#         # Code to execute if condition is false
#     Example:
#         1. Temperature = 78
#         2. if Temperature > 75:
#             print("It's quite warm today.")
#         else:
#             print("It's not very warm today.")

# The Elif Statement
#     Syntax:
#     if condition1:
#         # Code to execute if condition1 is true
#     elif condition2:
#         # Code to execute if condition2 is true
#     else:
#         # Code to execute if both conditions are false
#     Example:
#         1. score = 85
#         2. if score >= 90:
#             print("Grade: A")
#         elif score >= 80:
#             print("Grade: B")
#         else:
#             print("Grade: C or below.")
# You can place "if" statements inside other "if" statements. This is called nesting.
#     Example:
#         1. num = 10
#         2. if num > 0:
#             if num % 2 == 0:
#                 print("The number is positive and even.")
#             else:
#                 print("The number is positive and odd.")
#         else:
#             print("The number is not positive.")


# Exercise:
# 1. Write a program that checks if a number is positive, negative, or zero

#     Example:
#         1. num = int(input("Enter a number: "))
#         2. if num > 0:
#             print("The number is positive.")
#         elif num < 0:
#             print("The number is negative.")
#         else:
#             print("The number is zero.")







# # # Hands on #1 Exercise:1

# # num = int( input("Enter a number: "))
# # if num > 0: 
# #     print("The number is positive.")


# # Hands on #2 even or odd


# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")



# More Notes
# Python Scripts readh left to right, top to bottom, just like reading a book.
# Definitive Loop for a number ---FOR LOOP)

# Brackets indicated a list
#     Example: 
#         1. my_list = ['hello']
#         2. my_list.append('goodbye')
#         3. my_list.append(5)

#         My list is now 
#         print(my_list)
# #             ['hello', 'goodbye', '5']

# # List Indexing 
# # First item is assigned Index 0 
# # Next item is index 1, and continues on.
# # -1 Index is the last item of the list
# # -2 index would give us the second to last, and on and on

# # Range Function
# # range (stop)
# # Creates a list, but doesn't include the stop value
# # range(5) generates 0,1,2,3,4
# # range (2,7) 2,3,4,5,6
# # range (1, 10, 2,) generates 1,3,5,7,9


# # Loops 
# # for loops key word "for" loop variable "in" sequence

# # example:
# # fruits = ["apple", "banana", cherry]
# # for fruit in fruits:
# #     print (fruit)

# # "WHILE" Loop
# # # Execute a block until conditions aren't true



# # Ask the user to input an even integer number. If the user puts an odd number, print "This is an odd number" and then prompt the user for an even number.

# # user_number = int(input("Enter an even integer number: "))
# # while user_number % 2 == 1:
# #     user number = int(input(Enter an even integer number: ))

# # print(f"Good Job! You entered an even number, {user_number}")






# secret_number = 22
# count = 1

# user_guess = int(input("Guess an integer number: "))
# while user_guess != secret_number:
#     if count > 5:
#         break

#     if user_guess < secret_number:
#         print("Your guess was too low!")
    
#     else:
#         print("Your guess was too high!")

#     user_guess = int(input("Guess an integer number: "))
#     count += 1

# if user_guess == secret_number:
#     print(f"Congratulations, you guessed the correct number")
#     print(f"it took you {count} guessess")

# else:
#     print(f"Guess better next time")



# Hands-on Python Conditional statements


# 1 Check if a number is positive


# user_guess = int(input("Enter an integer number: "))

# if user_guess > 0:
#     print (f"The number is positive!")




# 2 Even or Odd

# user_guess = int(input("Enter an integer number: "))

# if user_guess % 2 == 0:
#     print ("Even")

# else:
#     print ("Odd")




# # # 3 Age Category 


# user_guess = int(input("Enter your age: "))

# if user_guess <13:
#     print ("Child")

# elif user_guess <20:
#     print ("Teenager")

# elif user_guess <= 64:
#     print ("Adult")

# else:
#     print ("Senior")




# 4 Compare two numbers


# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))

# if num1 > num2:
#     print (f"{num1} is large")

# elif num2 > num1:
#     print (f"{num2} is larger")

# else:
#     print ("The numbers are equal")






#5 Grade Convert



# user_number = int(input("Enter the number grade: "))

# if user_number >= 90:
#     print("A")

# elif user_number >= 80:
#     print("B")

# elif user_number >= 70:
#     print("C")

# elif user_number >= 60:
#     print("D")

# else:
#     print("F")






# #6 String Length Check


# user_number = input("Enter a word: ")
# user_length = len(user_number)

# if user_length > 10:
#     print("Long string")

# else:
#     print("Short string")




#7 Logical and operator


# number = int(input("Enter a number: "))

# if number >= 10 and number <= 20:
#     print("Number is in range")
# else:
#     print("Out of range")





# #8 Logical OR operator

# letter = input("Enter a letter: ").lower()

# if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#     print("Vowel")
# else:
#     print("Consonant")



#9 Leap Year Checker


# year = int(input("Enter the year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")




# #10 BMI Caculator


# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))

# bmi = weight / (height ** 2)

# if bmi < 18.5:
#     category = "Underweight"
# # elif bmi < 25.0:
# #     category = "Normal weight"
# # elif bmi < 30.0:
# #     category = "Overweight"
# # else:
# #     category = "Obese"

# # print(f"BMI: {bmi:.1f} - {category}")







# Hands-On #2


# # Exercise 11: Create and Print a List


# colors = ["red", "blue", "green"]

# for color in colors:
#     print(color)



# # #12 List Length 


# numbers = [5, 10, 15, 20, 25]
# length = len(numbers)

# print(f"The list has {length} items")




#13 Append a list 


# my_list = []

# my_list.append("Bob")
# my_list.append("James")
# my_list.append("Jim")
# my_list.append("Tim")
# my_list.append("Dan")

# print(my_list)



# #14 Loop Through a Range

# for i in range(1, 11):
#     print(i)




#15 Sum Numbers in a List

# numbers = [4, 7, 2, 9, 12]
# total_sum = 0

# for num in numbers:
#     total_sum += num

# print(total_sum)



# # 16 List Membership


# # available_fruits = ["apple", "banana", "orange", "mango"]
# # fruit = "banana"

# # if fruit in available_fruits:
# #     print("In stock")
# # else:
# #     print("Out of stock")



# 17 Count Even Numbers



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1

# print(f"There are {even_count} even numbers")







# 18 While Loop Countdown


# count = 10

# while count >= 1:
#     print(count)
#     count -= 1



#19 While Loop with Condition


# number = 1

# while number <= 100:
#     print(number)
#     number = number * 2




# #20 Creat a list with Range


# even_numbers = list(range(0, 21, 2))

# print(even_numbers)






