#!/usr/bin/python3
'#program that prints number from 0-99 '

"""Print numbers 0 to 99."""
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")