from typing import *


# Reminders:
#
# Project #2 is assigned -- it is due in two weeks
# CodingBat Homework is due this coming Friday
# Exam #2 Redos are due on Friday as well


# Dictionary Examples --

# The user will enter  words
# Each word will do into a dictionary, keyed on word length, with value the list
#   of words of that length
#
# We will exit when the user enters the word 'Exit'

def word_count() -> Dict[int, List[str]]:
    out_dict = {}  # we need to build a new, empty dictionary

    cont = True  # a flag; will switch to False when the user enters 'Exit'

    while cont:
        ans = input('Please enter a word ("Exit" to stop): ')
        if ans == 'Exit':
            cont = False
        else:
            leng = len(ans) # not required, but easier conceptually for me

            # we want to put this information into the dictionary
            # -- but we do not know if <leng> is currently a valid key!
            # -- this is a common issue when building a dictionary

            if leng not in out_dict:
                out_dict[leng] = []

                out_dict[leng].append(ans)
            #OR
            #
            # if leng not in out_dict:
            #     out_dict[leng] = [ans]
            # else:
            #     out_dict[leng].append(ans)

    return out_dict



# List remainder -- given a list of integers lst and integer n,
# each entry in the list has a remainder when divided by n
#
# We find this by using mod: entry % n
#
# Return a dictionary, keyed on the remainder, with value the entries
# in the list which correspond to that remainder.
#
# For example:
# lst [4, 6, 9, 3, 6, 11], and n = 3 should return:
# {0: [6, 9, 3, 6], 1: [4], 2: [11]}

def list_remainder(lst: List[int], n: int) -> Dict[int, List[int]]:
    out_dict = {}

    for entry in lst:
        rem = entry % n

        if rem not in out_dict:
            out_dict[rem] = []

        out_dict[rem].append(entry)


    return out_dict


#
# value_find():
# Suppose you have a dictionary d, which has keys which are strings and
# values a list of integers
#
# Given a particular integer n, we want to return a list of the keys
# for which n belong to their value:
#
# For example:
# d = {'a': [5, 1, 2, 3], 'b': [1, 2, 3, 4], 'c': [2, 4, 2], d: [1, 3, 5]}
# then value_find(d, 3) would return ['a', 'b', 'd'] and
# value_find(d, 2) would return ['a', 'b', 'c'] and
# value_find(d, 7) would return []

def value_find(d: Dict[str, List[int]], n: int) -> List[str]:
    out_lst = []

    for key in d:
        if n in d[key]:
            out_lst.append(key)

    return out_lst


# value_sum()
# given a dictionary d where the keys are strings (typically multiple characters)
# and values are a list of integers.
#
# Given a particular single character char, return a sum of all of
# the values in the lists whose key contains that char
#
#For example:
# d = {'apple': [3, 4, 6], 'banana': [1, 2, 3], 'pear': [2, 4]}
# then value_sum(d, 'a') would return 25
# value_sum(d, 'b') would return 6
# value_sum(d, 'e') would return 19
# value_sum(d, 'z') would return 0

def value_sum(d: Dict[str, List[int]], str) -> int:
    sum_so_far = 0

    for key in d:
        if str in key:

            for item in d[key]:
                sum_so_far += item
                



    return sum_so_far


## Heap Tracing Example ##
# Solution at:
# https://hendrix-my.sharepoint.com/:b:/g/personal/seme_hendrix_edu/EQAN9upaNOdPgMb-MYBXbMEBfgPta6XOR5zzL1J6VeGJYw?e=R00WZq
#
# def main1():
#     my_list = [2, 3, 5]
#     your_list = my_list
#
#     my_dict = {'a' : 7, 'f' : 5}
#     your_dict =  {'a' : 7, 'f' : 5}
#     i = 0
#     for key in my_dict:
#         if my_dict[key] in my_list:
#             my_dict[key] = 0
#             my_list[i] = 17
#         i += 1
#
#
#     print(my_list)
#     print(your_list)
#
#     print(my_dict)
#     print(your_dict)
#     print(i)
#
# main1()




####### Bigger Data Example
## Given a data file in the form    zipcode;state;city;type;location_type
# Construct a dictionary of the form --    state: [zipcodes]
# #
#
def zip_code1() -> Dict[str,List[str]]:
    zip_file = open('zipcodes.txt','r')
    zip_dict = {}
    header = True
    for line in zip_file.readlines():
        data = line.strip().split(';')
        if not header:
            zipc = data[0]
            state = data[1]
            city = data[2]
            zip_type = data[3]
            location_type = data[4]


            if state not in zip_dict:
                zip_dict[state] = []
            if zipc not in zip_dict[state]:
                zip_dict[state].append(zipc)

        header = False

    zip_file.close()

    return zip_dict
#







