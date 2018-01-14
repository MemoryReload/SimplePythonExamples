import os
import string


def replace(file, search_for, replace_with):
    back = os.path.splitext(file)[0] + ".bak"
    temp = os.path.splitext(file)[0] + ".tmp"
    try:
        # remove the old temp file
        os.remove(temp)
    except os.error:
        pass
    fi = open(file)
    fo = open(temp, "w")
    for s in fi.readlines():
        fo.write(string.replace(s, search_for, replace_with))
    fi.close()
    fo.close()
    try:
        # remove the old backup file
        os.remove(back)
    except os.error:
        pass
    os.rename(file, back)
    os.rename(temp, file)


if __name__ == "__main__":
    file = "~/Desktop/shabbyTest/test.txt"
    file = os.path.expanduser(file)
    replace(file, "A", "B")
