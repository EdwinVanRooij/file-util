#!/usr/bin/env python

# Import modules
import sys


def encrypt(text):
    result = ''
    count = 0
    for c in text:
        # Get the ascii character, add count, get the character
        current_char = ord(c)
        current_char += count
        result += chr(current_char)
        count += 1
    return result


def decrypt(text):
    result = ''
    count = 0
    for c in text:
        current_char = ord(c)
        current_char -= count
        result += chr(current_char)
        count += 1
    return result


# Start program
def main():
    if len(sys.argv) <= 0:
        print('Syntax: <encrypt/decrypt> <text>')
        return
    args = sys.argv[1:]

    option = args[0]
    text = args[1]
    if option == 'encrypt':
        encrypted = encrypt(text)
        print('Encrypted:', encrypted)
    elif option == 'decrypt':
        decrypted = decrypt(text)
        print('Decrypted:', decrypted)
    else:
        print('Syntax: <encrypt/decrypt> <text>')


# Call main method
if __name__ == '__main__':
    main()
