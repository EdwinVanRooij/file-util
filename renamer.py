#!/usr/bin/python
import os
import sys


def incorrect_syntax(arguments):
    """
    Determines whether or not the user entered a correct syntax
    :param arguments: commandline parameter
    :return: true or false
    """

    if len(arguments) is not 1:
        return True


def rename_files(source_dir, new_name):
    """
    Searches trough a directory, moves all files with given extension
    to target directory.
    :return:
    """
    for root_dir, subdirectories, files in os.walk(source_dir):
        # Absolute path of source directory
        root_dir_abs = os.path.abspath(root_dir)
        print('Checking in root directory {}...'.format(root_dir_abs))

        counter = 1

        # Loop trough every file in current directory
        for file in files:
            print('Checking file {}...'.format(file))
            real_new_name = '{}_{}'.format(new_name, counter)
            os.rename(file, real_new_name)
            counter += 1
            print('Renaming file to {}...'.format(real_new_name))


def main(args):
    """Main method run from commandline"""
    if incorrect_syntax(args):
        print(
            'Syntax error. Correct usage:\npython {} <new_name>'.format(
                os.path.basename(__file__)))
        return

    new_name = args[0]

    rename_files(os.getcwd(), new_name)

    print('\n')


if __name__ == "__main__":
    """Python native main method, pass all parameters but the first one, being the name of this script"""
    main(sys.argv[1:])
