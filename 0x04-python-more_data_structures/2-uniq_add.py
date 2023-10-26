#!/usr/bin/python3
import functools

def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum_list = functools.reduce(lambda a, b: a + b, new_list)
    return sum_list
