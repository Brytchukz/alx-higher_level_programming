#!/usr/bin/python3
# function that deletes keys with a specific value in a dictionary.
# created by bright


def complex_delete(a_dictionary, value):
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
