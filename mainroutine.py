
from expel_1 import FilePathTokenizer
import argparse

tokens = FilePathTokenizer()


parser = argparse.ArgumentParser(description='File Path Tokenizer')

parser.add_argument("-f", "--filepaths", nargs='+', type=str, help="Expects any number of file path arguments, wrapped in one set of quotes, example command line: $ python example.py -f 'filepath1 filepath2 filepath3' ")
parser.add_argument("-i", "--input", help="expects a file path to a file containing file paths")
parser.add_argument("-s", "--stdin", help="expects file paths on stdin")

args = parser.parse_args()

# this function is my solution to running arguments with the backwards slash character on the command line-
def argsplit(string_args):
    split_args = string_args[0].split()
    if not split_args:
        print("Filepaths cannot be an empty string")
    else:
        return(split_args)




# Main routine 
if args.filepaths:
    filepath_list = argsplit(args.filepaths)
    print(tokens.tokenize_file_paths(filepath_list))
elif args.input:
    print(tokens.tokenize_fd(args.input))
else:
    print('no args')
