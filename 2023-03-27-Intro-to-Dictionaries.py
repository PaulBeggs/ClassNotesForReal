from typing import *

# Reminders:
#
# Project #2 is assigned -- it is due in two weeks
# CodingBat Homework is due this coming Friday
# Exam #2 Redos are due on Friday as well



# In the Caesar's Secrets Lab you had to write a function to find
# the letter frequency. This was somewhat difficult, since you
# had to continually remember how to match the index and the location
# in a list -- is 't' index 20 or 21 or 19 or ...

# What if there was a better way!?!?!?

# Today, we will learn about a new data type in Python,
# a dictionary!!!!

# Think about a simple, real-world dictionary
# Each entry contains:
#   -- a key   -- that is the word you look up
#   -- a value -- information associated with that key (the definitions, etymology, etc)

# That is essentially how a Python dictionary works:

# Each entry is a pair of key (which can only be immutable: strings, integers, floats, tuples for us)
# and a value, which can be anything -- string, int, lists, even another dictionary

# One major advantage of a dictionary is that finding the key is easy

# Simple contrived example:

# First, look at a list, which lists the current enrollments
# in each of the 100-level CSCI classes:
# CSCI 150 01 (this class)
# CSCI 150 L1 (Dr. Stanley's Lab)
# CSCI 150 L2 (Dr. Yorgey's Lab)
# CSCI 151 01
# CSCI 151 L1

#lst = [30, 13, 17, 25, 25]

# is essentially the assignment
# 0 -> 30
# 1 -> 13
# 2 -> 17
# 3 -> 25
# 4 -> 25


# The indices 0, 1, 2, ... are the *keys*, while the
# enrollments are the *values*  Each key maps to a single value.
#
#  A dictionary is just an extension of this, except that instead of requiring
#  the keys to be consecutive integers starting at 0,
#  we can have *arbitrary* keys!
#
#
# Suppose that we did this:
# 'CSCI15001' -> 30
# 'CSCI150L1' -> 13
# 'CSCI150L2' -> 17
# 'CSCI15101' -> 25
# 'CSCI151L1' -> 25

# In the list version, we have to remember which index corresponds to
# which class -- that's difficult!

# It is much easier if the key has some *meaning* to the human programmer.

#  One important point:  The keys themselves must be immutable --
#  that is they can only be ints, str, floats, booleans
#   you cannot use a list or a dictionary as the key in a dictionary.

#  Okay, so now what:
#  The following is a dictionary for our classes:

csci_dict: Dict[str,int] = {'CSCI15001': 30, 'CSCI150L1': 13,
                            'CSCI150L2': 17, 'CSCI15101': 25, 'CSCI151L1': 25}

# Notice the syntax -- we use { curly braces } to tell Python
# # what follows is a dictionary
# # we separate the key and the value with a colon :
# print(csci_dict['CSCI15001'])
# print(csci_dict['CSCI150L2'])
# # Run this in the console and type:      csci_dict['CSCI151L1']
#
# #print(csci_dict['CSCI12301'])
#
# # You got an error, since the dictionary does not have a value for that key
# # -- this is like asking for
# #    s[6] when s = 'abc'.
#
# ##############
# # Modifying dictionaries
# ##############
#
# # You can directly modify the value for a key:
# csci_dict['CSCI15001'] = 24
# print(csci_dict)
#
# # You can add a new key/value pair:
# csci_dict['CSCI12301'] = 123
# print(csci_dict)
# # # You can delete a key / value pair by:
# del csci_dict['CSCI15001']
# print(csci_dict)
# #
# # print(csci_dict)
# #

csci_dict: Dict[str,int] = {'CSCI15001': 30, 'CSCI150L1': 13,
                            'CSCI150L2': 17, 'CSCI15101': 25, 'CSCI151L1': 25}
# # Iterate over all keys using for
#
# Editing a dictionary is possible, but being able to return back to the original values is possible.
# To be able to iterate through each key in the dictionary, (for this example, that would be 30, 13, 17, 25, 25)
# you would use this code:
#
# for k in csci_dict:
#     del csci_dict[k]
#
# print(csci_dict)
#
# To be able to save an edited dictionary, you should save it as a -new- variable first.
# # The number of keys in a dictionary is given by len(dictionary_name)
print(len(csci_dict))
#
print(list(csci_dict.keys() )) #will return a list of all keys in the dictionary
#
# print(csci_dict.keys())
#
#dictionary_name.values()  will return a list of all values (including any duplicates!)
print(csci_dict.values())

# to see if a key is in a dictionary, use in:
print('MATH13001' in csci_dict)
print('CSCI15001' in csci_dict)
print(12 in csci_dict)

print(12 in list(csci_dict.values()))

######## Important info with dictionaries
# Each key maps to a single value (which can be any one thing)
# To be able to delete information from a dictionary, simply use the 'del' function.
# -- a str, an int, a float, or even a list
#   or another dictionary!
# It is possible that multiple keys might have the same value, though

# You can easily look up by key.  You cannot look up by value
#  That is, given a key, we can ask the dictionary for its matching value.
# Given a value, we cannot directly ask the dictionary which key(s) it is associated with

# This is like a regular language dictionary:
#  It is easy to look up what a word means
#  It is difficult to use a dictionary to find a word which has a
#  specific given meaning


# Now, let's try to do the letter_freq count
#
def list_freq_count(s: str) -> List[float]:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    freq_list = [0] * 26
    for char in s.lower():
         if char in alphabet:
             ind = alphabet.index(char)
             freq_list[ind] += 1

    i = 0
    total = sum(freq_list)

    for entry in freq_list:
        freq_list[i] = freq_list[i] / total
        i += 1
    return freq_list
#
#
#
#
def dict_freq_count(s: str) -> Dict[str, float]:
    freq_dict = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in alphabet:
        freq_dict[char] = 0


    total = 0
    for char in s.lower():
        if char in alphabet:

            freq_dict[char] += 1
            total += 1

    for key in freq_dict:
        var = freq_dict[key]
        # freq_dict[key] /= total

    return freq_dict
#

# word_file = open('alice.txt','r')
# s = word_file.read()
# word_file.close()

# freq_list = list_freq_count(s)

# freq_dict = dict_freq_count(s)



