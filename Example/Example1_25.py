import os


def open(filename, mode="rb"):
    import __builtin__
    file = __builtin__.open(filename, mode)
    if file.read(5) not in ("GIF87", "GIF89"):
        raise IOError, "not a GIF file"
    file.seek(0)
    return file


if __name__ == "__main__":
    while True:
        file = raw_input("Please enter the gif file Path:\n")
        file = os.path.expanduser(file)
        if not os.path.isabs(file):
            file = os.path.abspath(file)
        if os.path.exists(file) and os.path.isfile(file):
            fp = open(file)
            print  len(fp.read()), "bytes"
            break
        else:
            print("the file path is not correct!")
