import os
import re

def index(dir):
    files = []
    dir_stack = [dir]

    while dir_stack:
        cudir = dir_stack.pop()
        for file in os.listdir(cudir):
            file_abs = os.path.join(cudir,file)
            if os.path.isdir(file_abs) and not os.path.islink(file_abs) and not re.match("^\.",file,re.MULTILINE):
                dir_stack.append(file_abs)
            else:
                files.append(file_abs)
    return files

if __name__ == "__main__":
    for file in index("."):
        print("{} size {}".format(file, os.path.getsize(file)))

