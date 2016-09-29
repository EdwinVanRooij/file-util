#!/usr/bin/env python

# Import modules
import os
import sys


# Start program
def main():
    args = sys.argv[1:]

    # Check for valid syntax. We need a file path and new name, if no valid syntax, end program and give correct syntax
    if len(args) != 2:
        print("Syntax: remake-renamer.py <filepath> <newname>")
        return
    else:
        rename_files(args[0], args[1])


# Loop trough all files in file path and rename, recursively
def rename_files(source_dir, new_name_raw):
    # Number to put behind new name
    index = 0

    # Loop trough files
    for root_dir, subdirectories, files in os.walk(source_dir):
        # Absolute path of source directory
        root_dir_abs = os.path.abspath(root_dir)
        print('Checking in root directory {}...'.format(root_dir_abs))

        # Loop trough every file in current directory
        for file in files:
            index += 1

            # Extract extension
            file_extension = os.path.splitext(file)[1]

            # Create new name
            new_name = new_name_raw + str(index) + file_extension

            # Rename
            print('Renaming {} to {}'.format(file, new_name))
            os.rename(file, new_name)


# Call main method
if __name__ == '__main__':
    main()
