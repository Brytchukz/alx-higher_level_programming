#!/usr/bin/python3
# function that replaces an element of a list at a specific position (like in C)
# created by bright


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
