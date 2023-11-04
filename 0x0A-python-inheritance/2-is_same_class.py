#!/usr/bin/python3
'''Module for is_same_class method.'''
def is_same_class(obj, a_class):
    """test if type of obj == a_class"""
    if type(obj) == a_class:
        return True
    """ returns true if type == type"""
    else:
        return False
