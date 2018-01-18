#coding=utf8
import os
import stat, time
from Example.Example1_32 import dump


def copy_file(src, dst):
    fi = open(src, "rb")
    fo = open(dst, "wb")
    s = fi.read(1024)
    while s:
        fo.write(s)
        s = fi.read(1024)
    fi.close()
    fo.close()


def copy_attrs(src, dst):
    st = os.stat(src)
    os.chmod(dst, stat.S_IMODE(st[stat.ST_MODE]))
    os.utime(dst, (st[stat.ST_ATIME], st[stat.ST_MODE]))


if __name__ == "__main__":
    while 1:
        infile = raw_input("Please enter the source file path:\n")
        infile = os.path.expanduser(infile)
        infile = os.path.abspath(infile)
        if os.path.exists(infile):
            break
        else:
            print("file doesn't exist, Please try agian.")

    outfile = raw_input("Please enter your destination file path:\n")
    outfile = os.path.expanduser(outfile)
    outfile = os.path.abspath(outfile)

    copy_file(infile, outfile)
    # copy_attrs(infile, outfile)
    # 所有用户可读写
    # os.chmod(outfile,int("777",8))
    os.chmod(outfile,stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
    #更多用户读写位控制见stat模块文档

    print("{} stat".format(infile))
    st = os.stat(infile)
    dump(st)
    print("- chmod : {}".format(oct(stat.S_IMODE(st[stat.ST_MODE]))))

    print("{} stat".format(outfile))
    st = os.stat(outfile)
    dump(st)
    print("- chomd : {}".format(oct(stat.S_IMODE(st[stat.ST_MODE]))))
