#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    ''' method that calculates the fewest number of 
    operations needed to result in exactly n H 
    characters in the file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pasted_chars = 1  # number of chars in the file
    clipboard = 0  # number of H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        # if nothing is copied yet
        if clipboard == 0:
            # copyall
            clipboard = pasted_chars
            # increment operations counter
            counter += 1

        # if nothing is copied yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted_chars  # remaining chars to Paste
        # check impossiblity by checking if clipboard
        # has more than needed to reach desired number
        # which also means num of chars in file is equal
        # or more than num in the clipboard.
        # in both situations it is impossible to achieve n of chars
        if remaining < clipboard:
            return 0

        # if cannot be devided
        if remaining % pasted_chars != 0:
            # paste current clipboard
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            # copyall
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 2

    # if desired result reached
    if pasted_chars == n:
        return counter
    else:
        return 0