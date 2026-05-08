#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    if my_list is None:
        return 0
    # set() funksiyası təkrar elementləri avtomatik silir
    unique_numbers = set(my_list)
    # sum() funksiyası çoxluğun elementlərini toplayır
    return sum(unique_numbers)
