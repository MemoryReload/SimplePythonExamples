import os
import time


def dump(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print("- size: {} bytes".format(size))
    print("- owner: {0} {1} ".format(uid, gid))
    print("- created: {}".format(time.ctime(ctime)))
    print("- last accessed: {}".format(time.ctime(atime)))
    print("- last modified: {}".format(time.ctime(mtime)))
    print("- mode: {}".format(oct(mode)))
    print("- inode/dev: {0} {1}".format(ino, dev))


if __name__ == "__main__":
    while (1):
        path = raw_input("Please input a file path:\n")
        path = os.path.expanduser(path)
        path = os.path.abspath(path)
        if os.path.exists(path):
            break
        else:
            print("the file doesn't exist!")

    st = os.stat(path)
    print("stat {}".format(path))
    dump(st)

    fp = open(path, "r")
    st = os.fstat(fp.fileno())
    print("fstat {}".format(path))
    dump(st)
    fp.close()
