'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # Base case – checks if there is a word
    if len(word) == 0:
        return 0

    # Check if "th" occurs within the word at the 0 and 1 index
    # If so, returns a recursive function checking occurences
    # after index 0 and 1 and then adding a count of 1 to
    # account for occurence at 0 and 1 index
    elif word[:2] == "th":
        return 1 + count_th(word[2:])

    # Else, return recursive function checking occurences
    # of "th" in the word after index 1
    else:
        return 0 + count_th(word[1:])
