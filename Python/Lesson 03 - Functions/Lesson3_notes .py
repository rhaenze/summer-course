


# Problem 1 - Print numbers 1 to 100. If number is divisible by 3, print "Fizz" If the number is divisible by 5 print "Buzz". If it is divisible by both, print "FizzBuzz"


# number = print(1,100)

# if (number % 3 == 0):
#     print ("Fizz"

# elif (number % 5 == 0):
#     print ("Buzz")

# else (number % 5 == 0) and (number % )

#     print("Not a leap year")





# # Teacher Way (Need to FIX)



# # for number in range(1,101):
# #     print(number)

# # if number % 3 == 0 and number % 5 == 0:
# #     print ("FizzBuzz")

# # elif number % 3 == 0:
# #     print("Fizz")

# # elif number % 5 == 0:
# #     print("Buzz")

# # else:
# #     print(number)





# # Problem 2 - Rock Paper Siccors example TEACHER WAY

# computer_choice = "rock"

# user_choice = input(Enter "Rock, paper, or siccors: ")

# if user_choice == "rock" and computer_choice == "paper":
#     print("You lose")

# elif user_choice == "rock" and computer_choice == "siccors"
#     print("You win")

# elif user_choice == "paper" and computer_choice 





# # Problem 3 Create a guessing game ***TOOK PHOTO TO COMPARE**

# 

# import random

# random_number = random.randint(1,100)
# user_number = int(input("Enter a number between 1 and 100: "))

# while user_number != random_number:
#     if user_number > random_number: 
#         print("You guessed too high")
#     else: 
#         print("You guessed too low")
#     user_number = int(input("Enter a number between 1 and 100: "))
#     count += 1

# print (f"Congrats, you guessed {random_number}, and it took you {count} tries!")







# MODULES



# PPT Example #1



# import random

# random_number = random.randint (1,100)

# if random_number < 50:
#     print("The number is less than 50")

# # elif random_number > 50:
# #     print("The number is greater than 50")

# # else:
# #     print("The number is 50")


# # # print(random_number)







# # # Functions In Class Exercies 1 


# # # # def rectangle_area (user_input1,user_input2)
# # # #     sum = user_input1 * user_input2
# # # #     return sum



# # # # Teacher typed


# # # def rect_area(len: int, wid: int) -> int:
# # #     return len * wid

# # # length = int(input("Enter the lenght: "))
# # # width = int(input("Enter the width: "))

# # # area1 = rect_area(length, width)
# # # print(area1)




# # # # # In class exercies #2 NEED TO CHECK WORKFLOW

# # # # def tip_function(total: float, percentage: float) -> float:
# # # #     percentage_by_100 = percentage/100
# # # #     tip_amount = total * percentage_by_100
# # # #     return tip_amount

# # # # tip1 = tip (100,25)
# # # # print(tip1)

# # # # tip2 = (200,50)
# # # # print(tip2)






# # # In Class Exercies #4 (characters prompt)




# # def has_more_characters ("user_input1", "user_input2")
# #     len

# # user_input1 = float("PLease enter your first string: ")
# # user_input2 = float("PLease enter your second string: ")






# # Teacher's code


# def has_more_characters(string1 : str, string2 : str) -> str:
#     length1 = len(string1)
#     lenght2 = len(string2)
#     if length1 > lenght2:
#         return string1
#     elif lenght2 > length1:
#         return string2
#     else:
#         return "They are equal"









# STUDY SESSION PRACTICE PROBLEMS 7/16/2026




# temp = float(input("What is the current temerapture?: "))
# raining = input("Is it raining ('yes'/'no'): ")

# if temp < 40:
#     output = "Wear a coat!"

# elif temp <= 60:
#     output = "Bring a jacket!"

# else:
#     output = "Enjoy the weather!"

# if raining == "yes":
#     output += "Bring an umprella"

# print(output)









# # # 2 FizzBuzz


# start = int(input("Enter the start value: "))
# stop = int(input("Enter the stop value: "))

# def fizzBuzz(beginning: int, end: int) -> None:
#     fizzBuzzes = 0
#     for number in range (beginning,end+1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#             fizzBuzzes += 1

#         elif number % 3 == 0:
#             print("Fizz")

#         elif number % 5 == 0:
#             print("Buzz")
        
#         else:
#             print(number)


# amount = fizzBuzz(start, stop)

# print(f"There are {amount} of fizzBuzzess in between and including {start} and {stop}.")





# # # 3 Password Check

digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def password_checker(password: str) -> str:
    hasdigit = false
    password_len = len(password)
    if password_len < 8:
        return "Weak"
    
    else:
        for letter in password:

            #Check if the letter is equal to a digit
            for digit in digit_list:
                if letter == digit:
                    hasDigit = True
                    break
            
                
            if letter not in == letter.upper():
                hasUpperCase = True


        if hasDigit and hasUpperCase: 
            return "Strong"
        
        else:
            return "Medium"


user_password = input("enter a password (Make it strong!): ")
password_strenght = password_checker(user_password)


while password_strenght != "Strong":
    print("The password strenght is {password_strenght}")
    user_password = input("enter a password (Make it strong!): ")
    password_strenght = password_checker(user_password)


print(f"This password is {password_strenght}, great job!")









# Problem 4 Grade Caculator ****CORRECT****





# def letter_grade(score: float) -> str:

#     if score >= 90:
#         return("A")

#     elif score >= 80:
#         return("B")

#     elif score >= 70:
#         return("C")

#     elif score >= 60:
#         return("D")

#     else:
#         return("F")


# students = int(input("How many grades are there to enter? "))
# total_scores = 0 


# for student in range(1, students+1):
#     score =float(input(f"Enter student #{student}'s score: "))
#     total_scores += score
#     print(f"Student #{student} got a letter grade {letter_grade(score)}")

# print(f"The class average was {total_scores/students}, this is a {letter_grade(total_scores/students)}")



