#!/usr/bin/python3
# function that raises a type exception.
# created by bright

raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
