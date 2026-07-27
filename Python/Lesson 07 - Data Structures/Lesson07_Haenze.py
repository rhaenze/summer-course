
#Problem 1.a
# Take the 5 highest signal values, sum them together, then divide by 10. The result is the target's grid coordinate."

# signals = []
# with open ("preclass_problem1_data.txt", "r") as in_file:
#     for line in in_file:
#         signal = int(line)
#         signals.append(signal)

# signals_sorted = sorted(signals, reverse=True)
# high_5 = signals_sorted[:5]
# coordinate = sum(high_5) / 10.0

# print(f"The coordinate is {coordinate}")


# Another way to write the above code 

# with open ("preclass_problem1_data.txt", "r") as in_file:
#     print(f"The coordinate is {sum(sorted(int(x) for x in in_file)[-5:]) / 10}")





#In Class Problem 2

#You are building a simple database for a military unit. Each soldier has a name, rank, and years of service. Your job is to store this information and write a function that lets the commanding officer quickly look up any soldier's details by their last name.
#Create a dictionary called unit where each key is a soldier's last name and each value is another dictionary containing "rank" and "years_of_service“
#Populate it with at least 5 soldiers Write a function lookup_soldier(unit, last_name) that takes the dictionary and a last name and prints the soldier's full profile, or a friendly message if the soldier is not found
#Write a function lookup_soldier(unit, last_name) that takes the dictionary and a last name and prints the soldier's full profile, or a friendly message if the soldier is not found



unit = {}
unit['Hernandez'] = {"rank": "Private", "years_of_service": 2}
unit['Johnson'] = {"rank": "Corporal", "years_of_service": 5}
unit['Williams'] = {"rank": "Sergeant", "years_of_service": 10}
unit['Brown'] = {"rank": "Lieutenant", "years_of_service": 15}
unit['Davis'] = {"rank": "Captain", "years_of_service": 20}


def lookup_soldier(unit, last_name):
    if last_name in unit:
        rank = unit[last_name]["rank"]
        years_of_service = unit[last_name]["years_of_service"]
        print(f"Found {last_name}: Rank: {rank}, Years of Service: {years_of_service}")


    else:
        print("Could not find soldier with last name")

user_input = input("Enter a soldier's last name to look up: ")
lookup_soldier(unit, user_input.strip())


