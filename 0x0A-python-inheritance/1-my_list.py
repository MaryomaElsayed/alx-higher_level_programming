#!/usr/bin/python3
"""Defines an inherited list class MyList."""
class Myclass(list):
    def __init__(self):
        super().__init__()

    def print_sorted(self):
                """Print a list in sorted ascending order."""
        print(sorted(self))
