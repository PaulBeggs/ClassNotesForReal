# Reminders:
#  -- Homework #4 is due on Friday
#  -- Exam #1 Redos are also do on Friday
#  -- Project #1 due week from Friday, 3/3

# First, to finish last week's tracing.


# Example 3: -- we got about halfway through example 3 in class
# We'll finish it up, and then do the others to start on Wednesday.

def aaa(x: int, s: str) -> int:
    z = 7
    if x < z and s < 'hello':
        z += 3
        print(f'My string is {s} and number is {x}.')
    else:
        z *= 4
        print(f'I do not like the number {x}.')
    return z

def bbb(x: int, y: int) -> int:
    if x < y:
        return y // x
    else:
        return x - y

def main3():
    x = bbb(7,2)
    print(aaa(x,'hi'))  ## we did these two lines
    print(aaa(bbb(3,14),'abcd')) ## We need to start here

#main3()


#Example 4

def while_ex(n: int) -> int:
    i = 0
    j = 0
    while i < n:
        j += i
        i += 1

    return j

def main4():
    print(while_ex(3))
    print(while_ex(4))

main4()


# And now strings:

# We have used strings a bit previously. A string is just an ordered list of characters

# Today we will learn how to work with and manipulate them

s = 'My string'
t = 'abcdefg'

# Concatenation:


#print(s + t)

#print(s * 3)


# We can access the individual characters of a string by their index.
# The first character has index 0. This is weird at first, but you get used to it.

# s = 'My string'
#      012345678 (2 = the space in-between the two words)
# t = 'abcdefg'
#      0123456
#print(s[3])
# = s
#print(s[0])
# = M
#print(s[5])
# = r
#print(t[3])
# = d

# slice
#print(t[1:4])
# = bcd (includes the first character, but not the last. It includes #1, but not the 4th letter (e))

# We can also get a 'slice' of a string:

#print(s[1:6])
# = y str
# The syntax is str[a:b] will return from index a to index b - 1.
# This is also weird, but again, you get used to it

#print(s[4:])  #starts at index 4, goes to end
# = tring

#print(s[:4])  # starts at index goes, goes up to, does not include 4
# = My s

#print(s[:])  # starts at 0, goes to end (i.e. the whole string)
# = My string

#print(s[4:4])
# not going to print anything. (prints '')


#print(s[-4]) # -4 is the 4th character from the end
# = r

#print(s[-1]) # prints the last character
# = g

#print(s[-4:-1])
# = rin

#print(s[-1:-4])
#print(s[5:2])
# no print for both

#Index Errors
#print(s[12])
# there is no character at index 12, thus an error will arise.

#print(s[-20])
# there is no character at index 20, thus an error will arise.

# Slices never produce index errors:
#print(s[100:103])
# = ''

#print(s)
#print(s[2:-3])
# returns ''

#print(s[-3:8])

#Even poorly formed slices:
#print(s[5:2])


# String Methods & Functions
# There are a number of built-in Python functions that act on strings
# Formally, most of these are called 'methods,' as they act on members
# of a data class (the 'str' class) and the members are formally called 'objects.'

# We'll return to this nomenclature later in the semester
# For now, you can think of them as built-in functions

# Length -- a function, which returns the number of characters in a string
# print(len(s))
# simply returns how many characters there are. Since s has 8 characters, it is going to return 8

# print(len('aaa'))
# returns 3

# print(len(''))
# returns 0

# The special string '' is the null string

# Other examples (these are all methods)

# upper:

# print(s.upper())
# returns 'MY STRING'

# # lower
# print(s.lower())
# returns 'my string'

# print(s) #notice that s.lower() and s.upper() don't actually change s

# print('fbXtR%& *'.lower())
# doesn't mess with the special characters. only regular characters.

# count

#print(s.count('y'))
# returns 1

# print('abcABCabcdeab'.count('b'))
# returns how ever many b's are in the string.

#print('abcABCabcdeab'.count('a'))

# find

# print(s.find('t'))
#
# print('abcdabcdabcde'.find('z'))

# replace

# print(s.replace('y','TTT'))
# replaces all the y's with TTT's. (e.g., MTTT string)

# print('abcdabcdabcd'.replace('b',"X"))


#print('12303'.isdigit())

#print('-12303'.isdigit())


def string_counter(s: str, char: str) -> int:
    count = 0
    i = 0
    while i < len(s):
        if s[i] == char:
            count += 1
        i += 1
    return count


def string_replace(s: str, old: str, new: str) -> str:
    new_str = ''
    i = 0
    while i < len(s):
        if s[i] == old:
            new_str += new
        else:
            new_str += s[i]

        i += 1

    return new_str
