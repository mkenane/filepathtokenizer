
from expel_1 import FilePathTokenizer
import argparse

tokens = FilePathTokenizer()


parser = argparse.ArgumentParser(description='File Path Tokenizer')

parser.add_argument("-f", "--filepaths", nargs='+', type=str, help="expects any number of file paths, one or more")
parser.add_argument("-i", "--input", help="expects a file path to a file containing file paths")
parser.add_argument("-s", "--stdin", help="expects file paths on stdin")


args = parser.parse_args()


if args.filepaths:
    print(args.filepaths)
    print(tokens.tokenize_file_paths(args.filepaths))
elif args.input:
    print(tokens.tokenize_fd(args.input))
else:
    print('no args')
