# Reminders:


# Project #1 is due next Friday, 3/3
#
# New CodingBat homework -- working with loops and strings
#   due next Wednesday, 3/1

# While Loop Practice
# Write a function sum_to which takes in a single non-negative integer
# n and returns the sum 0 + 1 + 2 + ... + (n)

# Build a code to solve this problem:
#   sum_to(4) must be something like 0 + 1 + 2 + 3 + 4
def sum_to(n: int) -> int:
    s: int = 0
    i: int = 0
    while i <= n:
        s += i
        i += 1

    return s


# Consider the following code, which we wrote on Wednesday:


def string_counter(s: str, t: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        if s[i] == t:
            count += 1
        i += 1
    return count

# While loops and strings

# i = 0
# while i < len(s):
#   do stuff
#   i += 1

# Example -- 'Explode' string -- given a string, print each
# of its characters, one at a time to the screen


def explode_str(s: str):
    i = 0
    while i < len(s):
        print(s[i])
        i += 1


# Now, let's try something new -- reverse a string
# that is, given a string s = 'abcde', we want to return 'edcba'


def reverse(s: str) -> str:
    new_str = ''
    i = 0
    while i < len(s):
        new_str = s[i] + new_str
        i += 1

    return new_str


# Write is_inorder(s: str) -- will take in a lower case word
# and return True if the characters all appear in alphabetical order
# repeated letters are ok:
# 'hiss' is True, as is 'art', but 'sleet' is False

# def is_inorder(s: str) -> bool:
#
#     i = 0
#     while i < len(s):
#         # check two character -- return False if not in order
#         if s[i] > s[i + 1]:
#             return False
#
#         i += 1
#
#     return True

# This code has problems with the word 'hiss'. There is no character between 3 and 4. Only doing 3 comparisons

def is_inorder(s: str) -> bool:

    i = 0
    while i < len(s):
        if s[i] > s[i + 1]:
            return False
        i += 1

    return True

# new int_input


def int_input(prompt: str) -> int:
    is_okay = False
    while not is_okay:
        answer = input(prompt)
        if answer.isdigit():
            is_okay = True
        elif answer[0] == '-' and answer[1:].isdigit():
            is_okay = True
        else:
            print('That is not a valid integer. Please try again.')

    return int(answer)
