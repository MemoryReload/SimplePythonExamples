import os
import re


def print_file_size(arg, dir, files, item=None):
    print(dir)
    sum = 0
    rm_dirs = []
    for file in files:
        path = os.path.join(dir, file)
        if os.path.isfile(path):
            file_size = os.path.getsize(path)
            print("\t{}, size {}".format(path, file_size))
            sum += file_size
        else:
            # print("\tdir {} ".format(file))
            if re.match("^\.", file, re.MULTILINE):
                # warnings: do not remove file when iterate files, or strange things will happen.
                rm_dirs.append(file)
    # remove the subdirectories not to walk through(hidden dir are not visited)
    for item in rm_dirs:
        files.remove(item)
    print("content_size: {}\n----------------------".format(sum))


os.path.walk(".", print_file_size, None)
