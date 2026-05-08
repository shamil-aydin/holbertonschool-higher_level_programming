#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None
    # max() funksiyası lüğətin dəyərlərinə görə (get metodu ilə) ən böyük açarı tapır
    return max(a_dictionary, key=a_dictionary.get)
