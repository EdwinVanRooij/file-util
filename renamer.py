import os
import sys

def rename():
    [os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]


def incorrect_syntax(arguments):
    """
    Determines whether or not the user entered a correct syntax
    :param arguments: commandline parameter
    :return: true or false
    """

    if len(arguments) is not 3:
        return True


def main(args):
    """Main method run from commandline"""
    if incorrect_syntax(args):
        print(
            'Syntax error. Correct usage:\npython {} <extension/{}> <directory_from> <directory_to>'.format(
                all_extensions_keyword, os.path.basename(__file__)))
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
