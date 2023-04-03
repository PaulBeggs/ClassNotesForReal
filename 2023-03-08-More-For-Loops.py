from typing import *
# Reminders:
#  * Exam #2 is on Monday
#  * Practice Exam is posted; we will talk about it on Friday
#  * Project #1 Redos due on Monday

# Grade Updates
# * I will send out two email grade updates later this morning:
#   -- CodingBat -- will list all CodingBat problems I have for you
#             'C' = you have completed that problem
#             'S' = you have started working, but not yet completed
#   -- All Assignments -- should list all assignments:
#      * 7 Homeworks (0 - 6) -- through that due today
#      * 5 Labs (0-4) -- though "Guess My Number"
#      * Exam #1
#      * Project #1

# Please let me know if you have questions or something seems to be wrong
#
# For midterm grades:
#   A = at least 12 Completes and all 14 assignments C or PC
#   B = at least 10 Completes, and at least 13 C or PC
#   C = at least 5 Completes, no more than 3 missing
#   D = at least 9 assignments turned in

# Coding Bat: Sample
def sum67(nums):
    sum = 0
    flag = True
    i = 0
    while i < len(nums):
        if nums[i] == 6:
            flag = False
        elif flag:
            sum += nums[i]
        elif nums[i] == 7:
            flag = True
        i += 1
    return sum


# Write functions which




# list_sum - given a list of integers, return the sum. Empty should return 0

#while loop version
def list_sum(lst: List[int]) -> int:
    i = 0
    sum_so_far = 0
    while i < len(lst):
        sum_so_far += lst[i]
        i += 1
    return sum_so_far


#for loop version
def list_sum(lst: List[int]) -> int:
    sum_so_far = 0
    for item in lst:
        sum_so_far += item

    return sum_so_far







#
#
#
#
#
#
#
#
#
#
# # string_find: given a string s, return True if character c is in the string
#
def string_find(s: str, c: str) -> bool:
    found = False
    for char in s:
        if char == c:
            found = True

    return found

# given a list of ints, return True if there are an even number of odd integers
def even_odds(lst: List[int]) -> bool:
    count = 0
    for item in lst:
        if item % 2 == 1:
            count += 1

    return count % 2 == 0
    # if count % 2 == 0:
    #     return True
    # else:
    #     return False

def even_odds_flag(lst: List[int]) ->bool:
    even_odd = True
    for item in lst:
        if item % 2 == 1:
            even_odd = not even_odd

    return even_odd






#
#


#
#




# given a list of integers, if item is a multiple of seven,
# replace it with item // 7

def sevens(lst: List[int]) -> List[int]:

    for item in lst:
        if item % 7 == 0:
            item = item // 7

    return lst

# the above does not work -- it does not change the values of anything *in* the list

def sevens2(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        if lst[i] % 7 == 0:
            lst[i] = lst[i] // 7

    return lst

# the above changes lst. What ifd you wanted to leave lst alone?

def sevens3(lst: List[int]) -> List[int]:
    new_list = []
    for item in lst:
        if item % 7 == 0:
            new_list.append(item // 7)
        else:
            new_list.append(item)
    return new_list

def sevens4(lst: List[int]) -> List[int]:
    new_list = lst
    for i in range(len(new_list)):
        if new_list[i] % 7 == 0:
            new_list[i] = new_list[i] // 7
    return new_list


# given a list of ints, return a new list with all multiples of seven *removed*

def remove_seven(lst: List[int]) -> List[int]:
    new_list = []
    for item in lst:
        if item % 7 != 0:
            new_list.append(item)

    return new_list




#### for loops -- important
# inside a for loop, you should not change either the value of the
# looping variable itself, nor the iterable that is being looped over!**

# ** It is ok to change an individual value in a list,
# ** do not change a string "in place" as you loop over the string