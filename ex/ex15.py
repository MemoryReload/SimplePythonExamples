# coding: utf-8

from sys import argv

script, fileName = argv

txt = open(fileName)

print "Here's your file %r:" % fileName
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)

print txt_again.read()
txt_again.close()

