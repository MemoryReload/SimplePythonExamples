# coding: utf-8
import os, re, string, mmap


def mapfile(filename):
    path = os.path.abspath(filename)
    file = open(path, "r+")
    size = os.path.getsize(path)
    return mmap.mmap(file.fileno(), size)


data = mapfile("squareRoot.py")
index = data.find("测试中文支持！")
print data[index-10:index+30]

m = re.search("测试中文支持！",data)
print m.start(), m.group()
