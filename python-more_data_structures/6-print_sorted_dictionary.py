#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    # Açarları əlifba sırası ilə sıralayırıq
    keys = sorted(a_dictionary.keys())
    # Sıralanmış açarlar üzərində döngü qurub çap edirik
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
