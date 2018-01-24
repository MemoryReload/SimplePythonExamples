import os
import re

def print_file_size(arg, dir, files, item=None):
    print(dir)
    sum = 0
    for file in files:
        path = os.path.join(dir, file)
        # path = os.path.expanduser(path)
        # path = os.path.abspath(path)

        if os.path.isfile(path):
            file_size = os.path.getsize(path)
            print("\tfile {}, size {}".format(file, file_size))
            sum += file_size
        else:
            # print("\tdir {} ".format(file))
            if re.match("^\.",file,re.MULTILINE):
                # filter the subdirectory to walk through(hidden dir are not visited)
                files.remove(file)
    print("content_size: {}\n----------------------".format(sum))


os.path.walk(".",print_file_size, None)