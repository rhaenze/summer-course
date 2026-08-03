###7/31/2026###


#----------------------------------------------------------------------------
#Palindrome instructor example
# ---------------------------------------------------------------------------

# def palindrome(input_str):

#     if input_str == "":
#         return True
#     if len(input_str) == 1:
#         return True

#     if input_str[0] != input_str[-1]:
#         return False


#     print("computing {input_str[1:-1]}")
#     result = palindrome(input_str[1:-1])
#     print(f"recived {result} for {input_str[1:-1]}")
#     return result


# print(palindrome("level"))
# print(palindrome("hello"))
# print(palindrome("3355"))
# print(palindrome("racecar"))



# # ----------------------------------------------------------------------------
# # Example 4: String to Integer
# # ----------------------------------------------------------------------------
# def string_to_int(s: str) -> int:
#     # Base case: single digit
#     if len(s) == 1:
#         return int(s)
    
#     # Recursive case: convert all but last digit, multiply by 10, add last digit
#     return string_to_int(s[:-1]) * 10 + int(s[-1])

# print()
# print("String to Integer:")
# print(f"string_to_int('1234') = {string_to_int('1234')}")
# print(f"string_to_int('99') = {string_to_int('99')}")
# print()





#----------------------------------------------------------------------------
# On your own class problem
#----------------------------------------------------------------------------

# Calculate the sum of a list of numbers using recursion.

# What is(are the base case(s)? 

    # if len(numbers) == 0
            #&
    # if len(numbers) == 1

# What is(are) the recursive case(s)?
 
   # return numbers[0] + sum_list(numbers[1:]) 

# Be careful about passing lists around
    
    #sum is a predefined function in python, so we will use sum_list instead of sum to avoid rewriting the built-in function.




def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]
    
    return numbers[0] + sum_list(numbers[1:])

# print()
# print("**Calculations below.** Sum of List:")
# print(f"sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])}")
# print(f"sum_list([]) = {sum_list([])}")
# print(f"sum_list([5]) = {sum_list([5])}")
# print(f"sum_list([3, 4, 5, 6]) = {sum_list([3, 4, 5, 6])}")
# print()

#another way to print the results of the sum_list function
print("**Calculations below.** Sum of List:")
print(sum_list([]))
print(sum_list([1,2,3]))
print(sum_list([1,2,3,4,5]))







