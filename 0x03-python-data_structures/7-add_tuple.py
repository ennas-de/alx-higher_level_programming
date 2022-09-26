#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lengA = len(tuple_a)
    lengB = len(tuple_b)
# check for tuple_a
    if lengA < 1:
        tuple_a = (0, 0)
    elif lengA < 2:
        tuple_a = (tuple_a[0], 0)

# check for tuple_b
    if lengB < 1:
        tuple_b = (0, 0)
    elif lengB < 2:
        tuple_b = (tuple_b[0], 0)

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
