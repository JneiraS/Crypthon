import getopt
import sys

from src.filecryptographer import *


def print_help():
    print("Usage: script.py [options]")
    print("Options:")
    print("  -h, --help            Show this help message and exit.")
    print(" -m, -- method=METHOD encrypt or decrypt.")
    print("  -p, --password=PASSWORD Specify a password.")
    print("  -i, --input=FILE       Specify an input file.")
    print("  -o, --output=FILE      Specify an output file.")


def process_command_line_arguments():
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
