
class FilePathTokenizer:

# check if there is a file at end of path
    def isFilename_found(self, filepath):
      parted = filepath.rpartition(".")
      if parted[0] == '':
        return False
      else:
        return True


# check if input path (windows format) is valid  -> path must be absoute, not relative
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

# check if input path (unix format) is valid  -> path must be absoute, not relative - this method isn't used since instructions indicated that only windows path are coming in - wrote it by mistake
    def isAbsoluteLinux(self, filepath):
      if filepath[0] != "/":
        return False
      elif ".." in filepath:
        return False
      else:
        return True

#deal with tokenizing the file name portion of a filepath i.e 'somefile.exe'
    def tokenize_file_only(self, filepath):
        file_only = filepath.rpartition("\\")[2]
        file_tokens = file_only.split('.')
        file_tokenized = [file_only, file_tokens[0], file_tokens[1]]
        return file_tokenized




  #tokenizing an entire filepath, both subfolders and filename
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

# takes in a list of filepaths and itirates over to tokenize
    def tokenize_file_paths(self, filepaths):
      tokenized = {}
      for single_filepath in filepaths:
          val = self.tokenize_file_path(single_filepath)
          tokenized[single_filepath] = val.get(single_filepath)
      return tokenized


# takes in a file descriptor/filepath to a text file containing a filepath on every line
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
















# ******************************* FIRST ATTEMPTS/REFACTORING ATTEMPTS THAT BROKE *******************************



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



# print(tokenize_fd("learning.txt"))
# print(tokenize_file_paths(["c:\windows\system32\drivers", "c:\windows\system32\drivers", "c:\windows\system32\svchost.exe", "notafile/path/because", "c:\windows\system32\svchost.exe"]))
# print(tokenize_file_path(":\windows\system32\svchost.exe"))
# print(tokenize_file_path("c:\windows\system32\drivers"))
# print(isAbsoluteLinux("/c:\windows\..system32\drivers"))
# print(isAbsoluteWindows("w:indows\system32\drivers"))
# print(tokenize_file_path("c:\windows\system32\svchost.exe"))
# print(tokenize_file_path("c:\windows\system32\drivers"))
# print(tokenize_file_only("c:\windows\system32\svchost.exe"))



# ******************************* TUTORIAL PRACTICE *******************************
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

# try:
#     myFile = open('some_file.txt')
# except IOError:
#     print("Oh my snakes and garters!")
