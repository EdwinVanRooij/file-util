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

    if len(arguments) is not 3:
        return True


def get_and_move_files(target_extension, source_dir, target_dir_absolute):
    """
    Searches trough a directory, moves all files with given extension
    to target directory.
    :param target_extension: extension of file to move
    :param source_dir: directory in which to look for files
    :param target_dir_absolute: directory to move files to
    :return:
    """
    for root_dir, subdirectories, files in os.walk(source_dir):
        # Absolute path of source directory
        root_dir_abs = os.path.abspath(root_dir)
        print('Checking in root directory {}...'.format(root_dir_abs))
        # Loop trough every file in current directory
        for file in files:
            print('Checking file {}...'.format(file))
            # Retrieve extension of current file
            extension = os.path.splitext(file)[1]
            # Check if extensions match OR if keyword for all extensions was entered
            if extension.lower() == target_extension.lower() or target_extension == all_extensions_keyword:
                # Get absolute file path
                file_path_abs = os.path.join(root_dir_abs, file)
                # Generate target file path
                abs_target_file = os.path.join(target_dir_absolute, file)
                # Check whether or not the target filepath is already taken
                if not os.path.exists(abs_target_file):
                    # Move the file
                    print('Moving file {}...'.format(os.path.basename(file_path_abs)))
                    os.rename(file_path_abs, abs_target_file)
                else:
                    print('Tried to move file {}, but file already exists.'.format(os.path.basename(file_path_abs)))


def main(args):
    """Main method run from commandline"""
    if incorrect_syntax(args):
        print(
            'Syntax error. Correct usage:\npython {} <extension/{}> <directory_from> <directory_to>'.format(
                os.path.basename(__file__), all_extensions_keyword))
        return

    extension = args[0]
    source_dir = args[1]
    target_dir = args[2]

    print('\nChecking for extension\t{}\nin directory\t{}\nmoving to\t{}\n'.format(extension, source_dir, target_dir))

    get_and_move_files(extension, source_dir, os.path.abspath(target_dir))

    print('\n')


if __name__ == "__main__":
    """Python native main method, pass all parameters but the first one, being the name of this script"""
    main(sys.argv[1:])
