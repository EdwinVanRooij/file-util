#!/usr/bin/python
import os
import sys

all_extensions_keyword = 'all'


def incorrect_syntax(arguments):
    """
    Determines whether or not the user entered a correct syntax
    :param arguments: commandline parameter
    :return: true or false
    """

    if len(arguments) is not 1:
        return True


def amount_of_files(source_dir):
    """
    Returns the amount of files in the given directory
    :param source_dir: the directory to search in
    :return:
    """
    count = 0
    for root_dir, subdirectories, files in os.walk(source_dir):
        # Loop trough every file in current directory
        for file in files:
            print(".", end="")
            count += 1
    return count


def main(args):
    """Main method run from commandline"""
    if incorrect_syntax(args):
        print(
            'Syntax error. Correct usage:\npython {} <directory>'.format(os.path.basename(__file__)))
        return

    source_dir = args[0]

    print('\n{}\n'.format(amount_of_files(source_dir)))


if __name__ == "__main__":
    """Python native main method, pass all parameters but the first one, being the name of this script"""
    main(sys.argv[1:])
