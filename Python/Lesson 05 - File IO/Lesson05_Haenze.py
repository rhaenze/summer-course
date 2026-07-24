# #Lesson 5 - Inputs and Outputs 7/22/2026


# #What is the purpose of user defined functions?
#     #Recycle or reuse code

# #How do you define a function, and how do you use it?
#     #Give it a label (def) and a call and that is how we define and use our function 





# #Pre Class Problem 1 - The ULTIMATE RPS Simulation (20 min)

# #Starting from scratch write a python script that allows you to play rock, paper, scissors against the computer.

# #However, in this version you will ask the user how many games they want to play to determine the overall winner.  The computer has other things to do, so it will only accept playing the best of 1 to 9 games.
# # Example:  How many games would you like to play to determine who is the ultimate winner? 
# # Implied:  User input can only be an odd number from 1 to 9.  Continue to ask the user to re-enter how many games they would like to play until the user meets these criteria.  
# # Also implied:  If the user wants to play the best of 3 games, and wins the first two, they do not need to play a third game.

# # Bonus:  Incorporate ASCII-ART and delays into your game to add some flare.


# game_list = [1, 3, 5, 7, 9]
# total_games = int(input("How many games would you like to play 1-9), odd number only: "))

# while total_games not in games_list:
#     print("Please enter an odd number between 1 and 9")
#     total_games = int(input("How many games would you like to play (1-9), odd numbers only: "))


# user_wins = 0 
# cpu_wins = 0 
# wins_needed = (total/games //2) + 1


# #Test 
# print(total_games)
# print(wins_needed)
# while user_wins < wins_needed and cpu_wins < wins_needed:
#     #Game logic
#     user_choice = get_user_choice()
#     cpu_choice = get_cpu_choice()





# #Rock, Paper, Siccors Code

# # computer_choice = "rock"
# # user_choice = input("Enter rock, paper, or scissors:  ")

# # if user_choice == "rock" and computer_choice == "paper":
# #     print("You Lose")

# # elif user_choice == "rock" and computer_choice == "scissors":
# #     print("You Win")

# # elif user_choice == "paper" and computer_choice == "scissors":
# #     print("You Lose")

# # elif user_choice == "paper" and computer_choice == "rock":
# #     print("You Win")

# # elif user_choice == "scissors" and computer_choice == "rock":
# #     print("You Lose")

# # elif user_choice == "scissors" and computer_choice == "paper":
# #     print("You Win")

# # else:
# #     print("You tie")



# # #### DIDNT FINISH, MUST LOOK ######





# # Pre Class Problem 3 – A simple function (20 min)


# # A = P(1+r/n) ^ nt        **Turn this math equation into a function**
# # A = Amount
# # P = Principal 
# # R = Interest Rate 
# # N = Number of times is compounded per year ***Was told N's default vaule is 1***
# # T = Time in years


# def money(principal: float, interest: float, t: int, n: int = 1) -> float:
#     return principal * (1+interest/n) ** (n * t)

# # print(money(1000, 0.0061, 10, 1))

# CORRECT CODE ABVOE. SHOWS RETURN INSTRUCTOR REQUESTED

# print(money(1000, 0.031, 10, 1))

# CORRECT CODE ABOVE. SHOWS RETURN INSTRUCTOR REQUESTED



#1 MANIPULATING FILES PRACTICAL : Write a Python script that will write 100 random integers ranging from 50 to 100 into a file.  Each integer should be on a separate line.


#Code to create file.txt with 100 random integers

# import random 
# with open('file.txt', 'w') as file:
#     for line in range(100):
#         random_number = random.randint(50,100)
#         file.write(str(random_number) + "\n")


#Open this file, find max, min, and average

with open('file.txt', 'r') as input_file:
    lines = input_file.readlines()
    # lines_stripped = [line.strip for line in lines]
    # print(lines)
    count = 0 
    min = 1000
    max = 0
    sum = 0
    for line in lines:
        amount = int(line)
        sum += amount
        count += 1 
        if amount > max:
            max = amount
        if amount < min:
            min = amount
    average = sum/count

print(f"Max: {max}, Min: {min}, Average: {average}")


## CODE ABOVE IS CORRECT. Will need to stop the code that creates the file if we want to get the same numbers. It is rewriting the file everytime so that is why we are getting a different average everytime.









