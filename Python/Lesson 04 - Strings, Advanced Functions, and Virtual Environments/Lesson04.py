# #We added another test repo
# How to add to new repo:
# git clone
# change cd to new repo 
# echo "Test" >> text.txt
# git add 
# git commit - m ".\text.txt"
# git push



# Creating Virtual Environement code 

# PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> python -m venv test_venv   (CREATES NEW Environement)
# PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> .\test_venv\scripts\activate (CODE TO ACTIVATE VIRTUAL Environement)
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> deactivate  (CODE TO deactivate virtual Environement)


# Creating a virtual Environement with a different python

# PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> rm -r .\test_venv\   (Remvoed virtual Environement created above)      
# PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> py -3.10 -m venv test_venv (created virtual Environement with python 3.10)
# PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> .\test_venv\scripts\activate
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> python --version
# Python 3.10.0



# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> pip install requests   (Installing PIP)


# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> pip install rich (Installing rich)

# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> python '..summer-course\python\Lesson 04 - String, Advanced Functions, and Virtual Environments\venv_testScript.py'



# PIP Freeze (Snapshot of our current programs??)
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> pip freeze
# certifi==2026.6.17
# charset-normalizer==3.4.9
# idna==3.18
# markdown-it-py==4.2.0
# mdurl==0.1.2
# Pygments==2.20.0
# requests==2.34.2
# rich==15.0.0
# urllib3==2.7.0
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> pip freeze >> requirements.txt  (Creates a text file in the repo)




# Creating a virtual Environement using a requirements text
# 1. PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> rm -r .\test_venv\
# 2. PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> py -3.10 -m venv test_venv
# 3. PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> .\test_venv\scripts\activate
# 4. (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> pip list     (Shows what is downloaded shown below)
# Package    Version
# ---------- -------
# pip        21.2.3
# setuptools 57.4.0

# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> pip install -r requirements.txt    (HOW TO INSTALL REQUIREMENTS FROM TXT SHOWN BELOW)

# Collecting certifi==2026.6.17
#   Using cached certifi-2026.6.17-py3-none-any.whl (133 kB)
# Collecting charset-normalizer==3.4.9
#   Using cached charset_normalizer-3.4.9-cp310-cp310-win_amd64.whl (162 kB)
# Collecting idna==3.18
#   Using cached idna-3.18-py3-none-any.whl (65 kB)
# Collecting markdown-it-py==4.2.0
#   Using cached markdown_it_py-4.2.0-py3-none-any.whl (91 kB)
# Collecting mdurl==0.1.2
#   Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
# Collecting Pygments==2.20.0
#   Using cached pygments-2.20.0-py3-none-any.whl (1.2 MB)
# Collecting requests==2.34.2
#   Using cached requests-2.34.2-py3-none-any.whl (73 kB)
# Collecting rich==15.0.0
#   Using cached rich-15.0.0-py3-none-any.whl (310 kB)
# Collecting urllib3==2.7.0
#   Using cached urllib3-2.7.0-py3-none-any.whl (131 kB)
# Installing collected packages: mdurl, urllib3, Pygments, markdown-it-py, idna, charset-normalizer, certifi, rich, requests
# Successfully installed Pygments-2.20.0 certifi-2026.6.17 charset-normalizer-3.4.9 idna-3.18 markdown-it-py-4.2.0 mdurl-0.1.2 requests-2.34.2 rich-15.0.0 urllib3-2.7.0




# CODE TO PULL STAGED FILES AND GRAY OUT REPO SO GIT DOESN'T TRACK IT (ADD INTO A SPERATE FILE)
# a_new_test_venv/


# CODE TO PULL STAGED FILES AND GRAY OUT REPO SO GIT DOESN'T TRACK IT

# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> git status
# On branch main
# Your branch is up to date with 'origin/main'.

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         .gitignore
#         requirements.txt

# nothing added to commit but untracked files present (use "git add" to track)
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> git status
# On branch main
# Your branch is up to date with 'origin/main'.

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         .gitignore
#         requirements.txt

# nothing added to commit but untracked files present (use "git add" to track)
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> git add .\.gitignore  
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> git status
# On branch main
# Your branch is up to date with 'origin/main'.

# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         new file:   .gitignore

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         requirements.txt

# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> git restore --staged .
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> git status
# On branch main
# Your branch is up to date with 'origin/main'.

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         .gitignore
#         requirements.txt

# nothing added to commit but untracked files present (use "git add" to track)
# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> 





# HoW TO SAVE A TXT FILE OF ALL CODE YOU HAVE DONE

# (test_venv) PS C:\Users\Haenze\Desktop\NOT A REPO\another_test_repo> history >> history.txt

# EXAMPLE: 
#   Id CommandLine                                                                                                                                               
#   -- -----------                                                                                                                                               
#    1 try { . "c:\Users\Haenze\AppData\Local\Programs\Microsoft VS Code\8a7abeba6e\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegr...
#    2 cd .\another_test_repo\                                                                                                                                   
#    3 .\test_venv\scripts\activate                                                                                                                              
#    4 pip list                                                                                                                                                  
#    5 pip freeze                                                                                                                                                
#    6 pip freeze >> requirements.txt                                                                                                                            
#    7 deactivate                                                                                                                                                
#    8 rm -r .\test_venv\                                                                                                                                        
#    9 rm -r .\test_venv\                                                                                                                                        
#   10 rm -r .\test_venv\                                                                                                                                        
#   11 py -3.10 -m venv test_venv                                                                                                                                
#   12 .\test_venv\scripts\activate                                                                                                                              
#   13 pip list                                                                                                                                                  
#   14 pip install -r requirements.txt                                                                                                                           
#   15 git status                                                                                                                                                
#   16 git status                                                                                                                                                
#   17 git status                                                                                                                                                
#   18 git status                                                                                                                                                
#   19 git revert .                                                                                                                                              
#   20 git restore .                                                                                                                                             
#   21 git status                                                                                                                                                
#   22 git restore .                                                                                                                                             
#   23 git revert .                                                                                                                                              
#   24 git restore --staged .                                                                                                                                    
#   25 git status                                                                                                                                                
#   26 clear                                                                                                                                                     
#   27 git status                                                                                                                                                
#   28 git status                                                                                                                                                
#   29 git add .\.gitignore                                                                                                                                      
#   30 git status                                                                                                                                                
#   31 git restore --staged .                                                                                                                                    
#   32 git status                                                                                                                                                
#   33 history.txt                                                                                                                                               
#   34 history.txt     
#   -->



# my_list = ['c', 'a', 't']
# my_string = "cat"

# print(my_list)







# my_list = ['c', 'a', 't']
# my_string = "cat"

# print(my_list)






# # String Practical Exercise

# #1. A website needs a function validate_username(username) that returns True if the username is valid and False otherwise. A valid username must:

# # Be between 5 and 15 characters long
# # Contain only letters, digits, or underscores
# # Start with a letter
# # Not end with an underscore
# # Contain at least one digit

# # Test cases:
# # validate_username("coder_42") → True
# # validate_username("2cool") → False
# # validate_username("hi") → False
# # validate_username("python_dev_") → False, validate_username("justletters") → False


# #Define the function

# def validate_username(username :str) -> bool:
#     length_req = False
#     numbers_letters_underscores = False
#     starts_with_letter = False
#     does_not_end_with_underscore = False
#     hasDigit = True


# # Be between 5 and 15 characters long
#     username_length = len(username)
#     if username_length > 5 and username_length < 15:
#         length_req = True

# # Contain only letters, digits, or underscores
#     if username == username.replace("_", "").isalnum():
#         num_letters_underscores = True

# # Start with a letter
# if username [0].isalpha():
#     starts_with_letter = True

# # Not end with an underscore
# if username [-1] != "_":
#     does_not_end_with_underscore = True


# # Contain at least one digit
# for char in username: 
#     if char.isdigit():
#         hasDigit = True

# # Function should return true or false based on criteria above

# if length_req and numbers_letters_underscores and starts_with_letter and does_not_end_with_underscore and hasDigit:


#         return true 
#     else:
#         return false



# NEED TO SEE HOW I FINISH THIS 





#2. Building My Own Moduel



# rectangle_area(length, width) -> area
# circle_area(radius) -> area
# tri_area(base, height) -> area




# 3 enumerate() Function Example (CORRECT CODE, RUNS PROBERLY)



#Write a function print_boarding_list(passengers) that prints each passenger with their seat number
# Seat 1: Lope
# Seat 2: Che
# Seat 3: Okafo
# Seat 4: Smit
# Seat 5: Patel

passengers_list = ["Lopez", "Chen", "Okafor", "Smith", "Patel"]

for index, passenger in enumerate(passengers_list, 1):
    print(f"Passenger {passenger} in seat {index}")







