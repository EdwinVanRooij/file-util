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

    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)

            index += 1

            # Extract extension
            filename, file_extension = os.path.splitext(full_path)

            # Create new name
            # Split the extension from the path and normalise it to lowercase.
            extension = os.path.splitext(filename)[-1].lower()
            if extension is not '':
                new_name_raw, file_extension = os.path.splitext(full_path)
                new_name = new_name_raw + str(index) + file_extension
            else:
                new_name = new_name_raw + str(index) + file_extension

            # Rename
            print('Renaming {} to {}'.format(full_path, new_name))
            os.rename(full_path, new_name)  # Call main method

            # # Loop trough files
            # for root_dir, subdirectories, files in os.walk(source_dir):


if __name__ == '__main__':
    main()
