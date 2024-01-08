#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ function to type"""
    if issubclass(obj, a_class):
        """return true if type == class"""
        return True
    else:
        return False
