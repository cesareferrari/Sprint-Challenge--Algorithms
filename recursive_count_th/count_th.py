'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

"""
base case:
    if string is less than 2 characters:
    it's not possible to have any th in it so return 0

recursive case:
   if char 0 and 1 [0:2] contain th:
        found one "th", increment count +1

       keep counting by recursively call same function 
       from next index and add the counter so far

    else: 
        keep counting recursively until length is less than 2
"""

def count_th(word):
    
    length = len(word)
    count = 0

    # base case
    if length < 2:
        return 0

    # recursive case
    if word[0:2] == "th":
        count += 1
        return count_th(word[1:]) + count
    else:
        return count_th(word[1:])

    
