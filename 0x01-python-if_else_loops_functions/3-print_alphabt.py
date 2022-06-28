#!/usr/bin/python3
'#program that prints the ASCII alphabet, in lowercase, except q and e '

for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
