# This file contains 3 topics:
#
#     * a short introduction to f-strings
#     * The Collatz/Hailstone Problems
#     * tracing, using the function stack -- there are three total examples given
#           and I have separately posted the completed traces on the Team page


# f-strings
# From Lab #4, you might have something like:

steps = 10
print('I guessed your number in ', steps, 'steps.')
# Though this works, we can make the ouput better
# by using a f-string (a "formatted string").

x = 5
t = 'hi there'
z = 12.4

print('I like the number ', x, '. ', t, ' and the number ',z)

print(f'I like the number {x}. {t} and the number {z}')

# the f-string lets you directly control the format, and you don't have to remember commas, spaces, etc.

#for today, we'll look at an old problem, the Collatz Conjecture:
# Given any positive integer, does the Hailstone function eventually reach 1?
# and if so, for each starting number, can we report back the number of steps.

# Let's plan this out:

# Query user for a positive integer
# Repeat until you get to 1:
#      run Hailstone
#      add one to the number of steps
# report back to the user the number of steps

# What functions might we use?
# A query user -- ask them what number they want to check
# hailstone -- which we have written before!
# a step-counter wrapper



# We wrote this first part in class on Wednesday

def pos_int_input() -> int:
    success = False # we call this a 'sentinel' value
    while not success:
        str_n = input('Please enter a positive integer: ')
        if str_n.isdigit():
            n = int(str_n)
            if n > 0:
                success = True

    return n

# We have written this previously

def hailstone(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

# This is new


def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        n = hailstone(n)
        steps += 1

    return steps


# We use a 'main' as the central control for our program

def main():
    init_n = pos_int_input()
    steps = collatz_steps(init_n)
    print(f'The integer {init_n} takes {steps} steps to reach 1.')


# The Function Stack

# The Function Stack is the fundamental way that Python controls which function
# is being run  during the execution of a file
# -- and how it deals with memory issues and variables.

# The stack works in a last-in, first-out mode.
# That is, the last item added to the stack if the first
# thing that gets processed.
# Once that happens, the next item is the second to last added, etc.

# Think of it like having a stack of books next to your bed.
# Every time you buy a new book, it goes on top
# When you read, you read whatever the top book is on the stack.
# If you finish that book,
# you put it aside and go to the next -- but even if you are in the middle of one
# when you buy a new book,
# the new book goes on top, and is what you read the next evening.

# (Solutions can be found: https://hendrix-my.sharepoint.com/:b:/g/personal/seme_hendrix_edu/EdGbc9_4A5BGmnLGBnC14o4BIxVj0r5zW-db6YZjd99wgA?e=iS3cpR

# Let's look at an example:



# Example 1:


def g(z: int):
    z =  z * 3
    print(z)


def f(x: int):
    g(x)
    g(x + 2)
    print(x)


#f(3)

# Notice that in this first example, neither g or f have explicit return values
# (print != return)



# Example 2:

def alice(z : int) -> int:
    if z > 0:
        return z * 2
    else:
        return z + 10

def bob(x : int, y : int) -> int:
    if y < x:
        return alice(x) + alice(y)
    else:
        return alice(x + y)

def main2():
    print(bob(6,7))

#main2()

# We then ran example 2.5, which changed main's print line to print(bob(8,-2))

def main25():
    print(bob(8,-2))

#main25()


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
    print(aaa(x,'hi'))
    print(aaa(bbb(3,14),'abcd'))

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

#main4()