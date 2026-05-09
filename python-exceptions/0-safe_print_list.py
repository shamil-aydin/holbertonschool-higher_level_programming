#!/usr/bin/python3
"""Module for safe list printing."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list safely.

    Args:
        my_list (list): The list to print from.
        x (int): Number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
