#!/usr/bin/python3
'#program that prints the ASCII alphabet, in lowercase, except q and e '

for letter in range(97, 123):
    if chr(letter) is != 'q' and chr(letter) is != 'e':
        print("{}".format(chr(letter)), end="")
