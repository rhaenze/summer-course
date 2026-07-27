# #Lesson 06 7/24


# Practice problem #1 - Interger Problem 

# # import random

# # with open('file.txt', 'w') as file:
# #     for line in range(100):
# #         random_number = random.randint(1,1000)
# #         file.write(str(random_number) + "\n")




# #Instructors Code

# import random

# with open('output.txt', 'w') as output_file:
#     for i in range(100):
#         random_number = str(random.randint(1,1000))
#         output_file.write(random_number + "\n")


# with open('output.txt', 'r') as input_file:
#     lines = input_file.readlines()
#     print(lines)

#     new_list = []
#     for line in lines:
#         lines = line.strip()
#         line = int(line)
#         new_list.append(line)
    
#     print(new_list)


#     lines_stripped = [int(line.strip()) for line in lines]
#     print(lines_stripped)

# min = 1000
# max = 0
# count = 0
# sum = 0

# for line in lines_stripped: 
#     if line > max:
#         max = line
    
#     if line < min:
#         min = line
    
#     average = sum/count


# print(f"Max: {max}, Min: {min}, Average: {average}")



# Pre Class Problem 2 - Creating a virtual environment (CODE BELOW!!!)

# (CHANGE CD to directory where we want to build the virtual enviornment)
# PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 06 - Error Handling> cd .. 
# PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python> cd '.\Lesson 04 - Strings, Advanced Functions, and Virtual Environments\'

#Code to create a new virtual environment
# PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments> python -m venv test_venv

#Code to activate scripts in environment 
# PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments>.\test_venv\scripts\activate

#Code checking what version python is running
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments> python --version
# Python 3.10.0

#installing the pre-made requirments documents wanted for this virtual environment
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments> pip install -r requirements.txt
# Collecting numpy==2.2.6
#   Downloading numpy-2.2.6-cp310-cp310-win_amd64.whl (12.9 MB)
#      |████████████████████████████████| 12.9 MB 2.2 MB/s                                                                      
# Collecting pandas==2.3.3
#   Downloading pandas-2.3.3-cp310-cp310-win_amd64.whl (11.3 MB)
#      |████████████████████████████████| 11.3 MB 930 kB/s                                                                      
# Collecting python-dateutil==2.9.0.post0
#   Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
#      |████████████████████████████████| 229 kB 3.3 MB/s                                                                       
# Collecting pytz==2026.2
#   Downloading pytz-2026.2-py2.py3-none-any.whl (510 kB)
#      |████████████████████████████████| 510 kB 3.2 MB/s                                                                       
# Collecting six==1.17.0
#   Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
# Collecting tzdata==2026.3
#   Downloading tzdata-2026.3-py2.py3-none-any.whl (348 kB)
#      |████████████████████████████████| 348 kB 1.6 MB/s                                                                       
# Installing collected packages: six, tzdata, pytz, python-dateutil, numpy, pandas
# Successfully installed numpy-2.2.6 pandas-2.3.3 python-dateutil-2.9.0.post0 pytz-2026.2 six-1.17.0 tzdata-2026.3

#Tried to updated PIP version code
# WARNING: You are using pip version 21.2.3; however, version 26.1.2 is available.
# You should consider upgrading via the 'C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments\test_venv\Scripts\python.exe -m pip install --upgrade pip' command.
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments> pip install --upgrade pip
# Requirement already satisfied: pip in c:\users\haenze\desktop\not a repo\summer-course\python\lesson 04 - strings, advanced functions, and virtual environments\test_venv\lib\site-packages (21.2.3)
# Collecting pip
#   Using cached pip-26.1.2-py3-none-any.whl (1.8 MB)
# Installing collected packages: pip
#   Attempting uninstall: pip
#     Found existing installation: pip 21.2.3
#     Uninstalling pip-21.2.3:
#       Successfully uninstalled pip-21.2.3
# ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'C:\\Users\\Haenze\\AppData\\Local\\Temp\\pip-uninstall-9bevut0o\\pip.exe'
# Check the permissions.


#Confirming that everything installed from the above steps
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments> pip list
# Package         Version
# --------------- -----------
# numpy           2.2.6
# pandas          2.3.3
# pip             26.1.2
# python-dateutil 2.9.0.post0
# pytz            2026.2
# setuptools      57.4.0
# six             1.17.0
# tzdata          2026.3
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments> 

# Then from the auto generated gitignore file that was created, we must add the below into the file so whatever is in the enviornment, doesn't get tracked to your GIT account

#   test_venv/

#"test_venv" is the name of the new enviornemnt I created. This could change based on what you name the enviornment. 






# Python Errors 7/24


#Errors are issues in a program that prevent it from running as expected

#They help programmers find and fix mistakes

#Why learn errors?
#Errors help you debug
#Knowing common errors makes writing and fixing code faster
#Good programs handle errors gracefully



#Code example using the try block that allows you to plan for errors gracefully

from area import rect_area

try:
    len = float(input("Enter the length:  "))
    wid = float(input("Enter the width:  "))
    rect_area(len, wid)

#The below code shows that if a value error occurs, not to crash the program, but to print this. This would happen if the user but in a letter for example for width.
except ValueError:
    print("There was some sort of error")

else: 
    print("No errors!!!")

#This code is telling the script to run instead of pushing a syntex error message
print("The main.py did not crash")


# Else and finally options aren't madatory but are optional code that can be added into to make the program run 


