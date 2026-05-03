#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples containing 2 integers each."""
    # Hər iki tuple-ı ən azı 2 elementi olacaq şəkildə genişləndiririk (0-lar əlavə etməklə)
    # Sonra yalnız ilk iki elementi götürürük
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    res_1 = a[0] + b[0]
    res_2 = a[1] + b[1]

    return (res_1, res_2)
