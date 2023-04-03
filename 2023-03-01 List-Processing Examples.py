import typing

# Join() -- the opposite of split: str.join(list) will return a string with
# the value of str between each entry
# Only works if th original list is made up of string entries

new_list = ['apples','bananas','pears','oranges','tangerines']
# new_string = '; '.join(new_list)
# print(new_string)


# word_list = ['dog']
# word_list.append('dot')
# word_list,append('lot')
# word_list.append('let')
# print(word_list)
# print ('->'.join(word_list))


# list processing:

# given a list of integers, return their sum
def list_sum(lst: list[int]) -> int:
    i = 0
    our_sum = 0
    while i < len(lst):
        our_sum += lst[i]
        i += 1
    return our_sum

# given a list of integers, return their product:
# if you want to multiply: change our_sum to our_prod; then our_prod = 1; and our_prod *= lst[i]

# given a list of integers, lst, a single integer n,
# count how many integers in lst are smaller than n
def small_count(lst: list[int], n: int) -> int:
    counter = 0
    i = 0
    while i < len(lst):
        if lst[i] < n:
            counter ++ 1
        i += 1

    return counter


# given a list of strings, each of which is a single lower case word, return True if the list is in alphabetical order

def alpha_order(lst: list[str]) -> bool:
    i = 0

    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            return False
        i += 1

    return True

# given a list of integers, return a new list which each element tripled
def triple_list(lst: List[int]) -> List[int]:
    new_lst = []
    i = 0

    while i < len(lst):
        new_lst.append(lst[i] * 3)
        i += 1

    return new_lst

# or change 'new_lst = []' to 'new_lst = lst'. Afterward, change 'new_lst.append(lst[i] * 3' -> 'new_lst * 3'.
# This does not work.

# write app_or_rem(lst: List[str], s: str) -> List[str]
# given a list of strings, lst, and a string, s
# return a new list where:
#  -- if s was not in lst, s should be appended
#  -- if *was* in lst, then s should be removed
#
# for example:
# lst = ['dog','cat','fish'] and s = 'turtle'
# would return ['dog','cat','fish', 'turtle']
#
# but
# lst = ['dog','cat','fish'] and s = 'cat'
# would return ['dog','fish']