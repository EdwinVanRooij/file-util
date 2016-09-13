#!/usr/bin/python
import os
import sys

# def incorrect_syntax(arguments):
# """
#     Determines whether or not the user entered a correct syntax
#     :param arguments: commandline parameter
#     :return: true or false
#     """
#
#     if len(arguments) is not 1:
#         return True
#
#
# def rename_files(source_dir, new_name):
#     """
#     Searches trough a directory, moves all files with given extension
#     to target directory.
#     :return:
#     """
#     for root_dir, subdirectories, files in os.walk(source_dir):
#         # Absolute path of source directory
#         root_dir_abs = os.path.abspath(root_dir)
#         print('Checking in root directory {}...'.format(root_dir_abs))
#
#         counter = 1
#
#         # Loop trough every file in current directory
#         for file in files:
#             print('Checking file {}...'.format(file))
#             old_name = file
#             filename, file_extension = os.path.splitext(file)
#            real_new_name = '{}_{}{}'.format(new_name, counter, file_extension)
#            os.rename(file, real_new_name)
#            counter += 1
#            print('Renaming file {} to {}...'.format(old_name, real_new_name))


import os.path


def rename_files(paths, new_name):
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                extension = os.path.splitext(filename)[1]
                print('Would rename {} to {}...'.format(filename, new_name))
                #os.rename(filename, new_name)


def main(args):
    """Main method run from commandline"""
    if len(args) is not 2:
        print(
            'Syntax error. Correct usage:\npython {} <directory> <new_name>'.format(
                os.path.basename(__file__)))
        return

    directory = args[0]
    new_name = args[1]

    rename_files(directory, new_name)

    print('\n')


if __name__ == "__main__":
    """Python native main method, pass all parameters but the first one, being the name of this script"""
    main(sys.argv[1:])
