# Basic Algorithms

# Exercise 1

# What is the output of this block of code?

#My Answer:
    # 1, 2, 3
    # hi, b, c
    # do-re-mi


# def mut_example(list1, list2, list3):
#     if len(list1) > 2:
#         list1 = list1[:2]     # shallow copy (new list)
#     list2[0] = "hi"           # modify in place
#     list3 = "".join(list2)    # creates a new list 

# a_list = [1, 2, 3]
# b_list = ["a", "b", "c"]
# a_str = "do-re-mi"
# mut_example(a_list, b_list, a_str)
# print(a_list)
# print(b_list)
# print(a_str)





# Exercise 2

# What's the difference between sort and sorted?

# Which one is a list method and which one is a function that works on lists?

# Please explain


#My answer: 
#Sort is an action of operating on a list. Changes original copy
#Sorted takes a list as input and returns a sorted/new copy. Will need to assign this copied list somewhere. 


# Exercise 3

# Write a function that doubles the elements in a list.

#assuming in place 
def double_list(in_list)
    for index in range(len(in_list))
        in_list[index] = in_list[index] * 2


#not in palce 
def double_list_two(in_list):
    return [x * 2 for x in in_list]


def double_list_three(in_list)
    new_list = []
    for elem in in_list:
        new_list.append(elem * 2_)
    return new_list




# Write a function that doubles the elements in a tuple.

def double_tuple(in_tuple):
    return tuple(x * 2 for x in in_tuple)




# Exercise 4

# Rewrite the pop, count, extend, reverse, and sort functions

def my_pop(in_list)
    new_val = in_list[-1]
    del in_list[-1]
    return new_val

def my_len(in_list):
    count = 0
    for elem in in_list:
        count += 1
    return len


def my_count(in_list, obj):
    count = 0 
    for elm in in_list:
        if obj == elem:
            count += 1

    return count


def my_exten(in_list, other_list):
    for elem in other_list:
        in_list. append(elem)



def my_reverse(in_list)
    reversed = []
    for elem in in_list[::-1]
        reversed.append(elem)
    return reversed 

#or 

def my_reverse_two(in_list):
    for index in range(len(in_list) // 2):
        in_list[index], in_list[-index - 1] = in_list[-index - 1], in_list[index]




def bubble_sort(in_list)






# Return the results in a new list and do not modify the original list

# (do not use the function you are rewriting)


# Exercise 5

# Fractions can be reprsented by the tuple (numerator, denominator)

# Write a function that adds two fractions



# Write a function that multiplies two fractions


# Write a function that simplifies a fraction


# Exercise 6

# write a function to calculate distance between two cartesian coordinates



# extension: make it work for more than two dimensions

