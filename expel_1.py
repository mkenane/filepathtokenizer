
class FilePathTokenizer:
    # def __init__(self):
    #     self.tokens = {}
# check if there is a file at end of path


    def isFilename_found(self, filepath):
      parted = filepath.rpartition(".")
      if parted[0] == '':
        return False
      else:
        return True

# check if input is valid  -> path must be absoute, not relative
    def isAbsoluteLinux(self, filepath):
      if filepath[0] != "/":
        return False
      elif ".." in filepath:
        return False
      else:
        return True

    def isAbsoluteWindows(self, filepath):
        
        drives = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if filepath[0] not in drives:
            return False
        elif filepath[1:3] != ":\\":
            return False
        elif ".." in filepath:
            return False
        else:
            return True

    #  !!!!!! need to change to take in full filepath with a file
    # def tokenize_subfolders(subfolders):
    #     tokens = subfolders.split('\\')
    #     remove_drive = subfolders.split(':\\')[1].replace("\\", "/")
    #     tokens.append(remove_drive)
    #     tokenized = {subfolders: tokens}
    #     return tokenized

    # def tokenize_subfolders_v2(filepath):
    #     remove_file = filepath.rpartition('\\')[0]
    #     print(remove_file)
    #     tokens = remove_file.split('\\')
    #     remove_drive = remove_file.split(':\\')[1].replace("\\", "/")
    #     tokens.append(remove_drive)
    #     return tokens


    def tokenize_file_only(self, filepath):
        file_only = filepath.rpartition("\\")[2]
        file_tokens = file_only.split('.')
        file_tokenized = [file_only, file_tokens[0], file_tokens[1]]
        return file_tokenized





    def tokenize_file_path(self, filepath):

      if not self.isAbsoluteWindows(filepath):
        return {filepath: "filepath input invalid"}
      else:
        if not self.isFilename_found(filepath):
          tokens = filepath.split('\\')
          remove_drive = filepath.split(':\\')[1].replace("\\", "/")
          tokens.append(remove_drive)
          tokenized = {filepath: tokens}
          return tokenized
        elif self.isFilename_found(filepath):
          file_only = self.tokenize_file_only(filepath)
          remove_drive_and_file = filepath.split(':\\')[1].replace("\\", "/").rpartition("/")[0]
          tokens = filepath.split('\\')
          tokens.pop()
          tokens.append(remove_drive_and_file)
          file_only = self.tokenize_file_only(filepath)
          full_filepath_tokenized = tokens+file_only
          tokenized = {filepath: full_filepath_tokenized}
          return tokenized
        # print(remove_drive_and_file)
        # print(tokens)
        # print(file_only)
        # print(full_filepath_tokenized)


    def tokenize_file_paths(self, filepaths):
      tokenized = {}
      for single_filepath in filepaths:
          val = self.tokenize_file_path(single_filepath)
          tokenized[single_filepath] = val.get(single_filepath)
      return tokenized

# try:
#     myFile = open('some_file.txt')
# except IOError:
#     print("Oh my snakes and garters!")

    def tokenize_fd(self, fd):
        filepaths = []
        try:
            my_handle = open(fd)
        except (OSError, IOError):
            print("file not found")

        else:
            with open(fd) as my_handle:
                paths = [x.replace('\n', '').replace('"', '') for x in my_handle.readlines()]
                for p in paths:
                    filepaths.append(p)
                    my_handle.close()
                    return self.tokenize_file_paths(filepaths)

# print(tokenize_fd("learning.txt"))
# print(tokenize_file_paths(["c:\windows\system32\drivers", "c:\windows\system32\drivers", "c:\windows\system32\svchost.exe", "notafile/path/because", "c:\windows\system32\svchost.exe"]))
# print(tokenize_file_path(":\windows\system32\svchost.exe"))
# print(tokenize_file_path("c:\windows\system32\drivers"))
# print(isAbsoluteLinux("/c:\windows\..system32\drivers"))
# print(isAbsoluteWindows("w:indows\system32\drivers"))
# print(tokenize_file_path("c:\windows\system32\svchost.exe"))
# print(tokenize_file_path("c:\windows\system32\drivers"))
# print(tokenize_file_only("c:\windows\system32\svchost.exe"))




# for line in file:
# print line,


#
#
# print(tokenize_fd("learning.txt"))

#  !!!!!! need to change to take in full filepath with a file
# def tokenize_subfolders(subfolders):
#     tokens = subfolders.split('\\')
#     remove_drive = subfolders.split(':\\')[1].replace("\\", "/")
#     tokens.append(remove_drive)
#     tokenized = {subfolders: tokens}
#     return tokenized

# def tokenize_subfolders_v2(filepath):
#     remove_file = filepath.rpartition('\\')[0]
#     print(remove_file)
#     tokens = remove_file.split('\\')
#     remove_drive = remove_file.split(':\\')[1].replace("\\", "/")
#     tokens.append(remove_drive)
#     return tokens






# def tokenize_file_paths(file_paths):

# tokenize_file_paths(file_paths):
# + Input - List of file paths
# + Output - Returns a dict where the key is the original file path,
# and the value is a list of tokens extracted from the file path
#
#
# tokenize_fd(fd):
# + Input - A file descriptor that points to a text file where each
# line of the text file is a new file path
# + Output - Returns a dict where the key is the original file path,
# and the value is a list of tokens extracted from the file path
#
#
# tokenize_file_path(file_path):
# + Input - A single file path as a string
# + Output - Returns a dict where the key is the original file path,
# and the value is a list of tokens extracted from the file path
#
#
# Make sure you have unit tests for all functions you write.
#
# How To Tokenize:
#
#
# Tokenization should break each sub folder out into its own item in the list,
# it should also fabricate a token that contains all the directories excluding drive and filename:
#
#

#
#
# If a filename is found tokenization should be as follows:
#
#
# [<filename>.<ext>, <filename>, <ext>]
#
#
# Example:

#
#
# To be valid input, the file path must be absolute, not relative.
#
#
#
#
# Delivery:
# Please put this object in its own file. Create a second file where you implement a main routine (use argparse) that takes the following arguments:
#
#
# -f or --filepaths | expects any number of file paths. You may assume that the file path is properly escaped for the platform on which it is running.
# -i or --input | expects a file path to a file containing file paths
# -s or --stdin | expects file paths on stdin
#
#
# Your main routine should parse the arguments and call the corresponding methods on the FilePathTokenizer object, you should print the results to screen.
#

#
# - Your program / test execution
# - python --version (so we know what version you ran against)
#
## my_handle = open("learning.txt")
# print(my_handle.readline(8))
#
# my_file=open("D:\\new_dir\\multiplelines.txt","r")
# Use print to print the line else will remain in buffer and replaced by next statement
# for line in my_file:
#     print(line)
# my_file.close()
#
# def testing():
#     my_handle = open("learning.txt")
#     for line in my_handle:
#         print(line)
#         print("next line")
#     my_handle.close()
#
# testing()
