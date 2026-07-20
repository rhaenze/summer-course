#It's about the problem solving process 

    #1) Write inputs, outputs, and do your best to fill in the middle. Do this with comments, NOT CODE.
    #2) DO the smallest amount of work, and test it, rinse and repeat. Translate your comments into code.
    #3) Build intelligent test cases, and test thoroughly. Ask yourself why things are happening










# #Problem 1   ****NEED TO CHECK AND FINISH***

# #Get the users name
# name_sentence = int(input("What is your name? "))

# #get their favorite number 
# favorite_number = int(input("What is your favorite number? "))

# #define a dunction that creates a personalized card based on the user's input
#     def personalized_card(symbol: str, name: str, favorite_number: int) -> None:
# #inside of the fuction, create both sentences
# name_sentence = "Hello, " + name
# number_sentence = "Your favorite number is" + str(favorite_number)
# sentence_1_len = len(name_sentence)
# sentence_2_len = len(number_sentence)

# sentence_len_diff = abs(sentence_2_len - sentence_1_len)

# if sentence_1_len >= sentence_2_len
#     max_len = sentence_1_len

# else:
#     max_len = sentence_2_len


# #Take a lenght of both, and compare them. The longest sentnece is going to drive the size of the card
# #Create the card based on that
# #print the card


# #call a function that creates a personalized card 


# print(symbol * (max_len + 6))
# print(symbol + "  " + name_sentence + "  " * sentence_len_diff + "  " + symbol)
# print(symbol + "  " + number_sentence + "  " + symbol)
# print(symbol * (max_len + 6))







# # Problem 2 Sequence Explore 


# print(list(range(1,16)))
# print(list(range(2,31,2)))
# print(list(range(20,-1,-1)))




# for i in range(1,16):
#     print(i, sep= " ", end=" ")

# print()

# for j in range(2,31,2):
#     print(j, sep= " ", end=" ")

# print()


# for k in range(20, -1, -2):
#     print(k, sep= " ", end=" ")


# print()


# def print_range(start: int, stop: int, step: int) -> None:
#     for number in range(start, stop, step):
#         print(number, sep=" ", end= " ")

# #*****THE CODE'S ABOVE IS THE SAME OUTPUT AS THE BELOW CODE****

# print_range(20,-1,-2)










# Problem 4 ****CORRECT****




#Ask the user for:

#The distance of the trip in miles
distance = int(input("What is the trip distance in miles? "))


#Their car's fuel efficiency in miles per gallon (MPG)

user_MPG = float(input("What is your car's miles per gallon? "))

#The current price of gas per gallon in dollars

current_gas_price = float(input("What is the current price of gas per gallon? "))

#Calculate and print:

#The number of gallons needed (rounded to 2 decimal places)

gallons_needed = round(distance/user_MPG,2)
total_fuel_cost = gallons_needed * current_gas_price
#The total fuel cost (rounded to 2 decimal places)


print("\n\n")


print('--- Road Trip Fuel Estimate ---')
print(f"Distance: \t {distance} Miles")
print(f"Fuel efficiency: {user_MPG} MPG")
print(f"Gas Price:\t {current_gas_price} / Gallon")

# \t is basically a tab to align things when it prints in PYTHON. 

print()

print(f"Gallons Needed: {gallons_needed: .2f} Gallons")
print(f"Total Fuel Cost: ${total_fuel_cost:.2f}")





