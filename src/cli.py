import getopt
import sys

from src.filecryptographer import *


def print_help() -> None:
    """
    Prints a help message to the standard output, detailing the usage of the script and the available
    command-line options.
    """
    print("Usage: script.py [options]")
    print("Options:")
    print("  -h, --help            Show this help message and exit.")
    print(" -m, -- method=METHOD encrypt or decrypt.")
    print("  -p, --password=PASSWORD Specify a password.")
    print("  -i, --input=FILE       Specify an input file.")
    print("  -o, --output=FILE      Specify an output file.")


def process_command_line_arguments() -> None:
    """
    Parses command-line arguments and processes a file accordingly.

    This function parses command-line options to extract parameters such as the operation mode (encryption
    or decryption).
    password, input file path, and output file path. Based on these parameters, it creates an instance of
    FileCryptographer and performs the specified operation on the input file, saving the result to the
    output file.
    """
    password = None
    input_file = None
    output_file = None
    method = None

    try:
        options, args = getopt.getopt(sys.argv[1:], "hm:i:o:",
                                      ["help", "method=",
                                       "input=",
                                       "output="])
    except getopt.GetoptError as err:
        print(str(err))
        print_help()
        sys.exit(2)

    for opt, arg in options:
        if opt in ("-h", "--help"):
            sys.exit()
        elif opt in ("-m", "--method"):
            method = arg
        elif opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-o", "--output"):
            output_file = arg

    process = FileCryptographer(password, input_file, output_file)

    if method == "enc":
        process.encrypt_file()
    else:
        process.decrypt_file()