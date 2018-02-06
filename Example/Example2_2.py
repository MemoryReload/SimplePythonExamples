import fileinput
import glob
import sys

for line in fileinput.input(glob.glob("./Example/Example1_?.py")):
    if fileinput.isfirstline():
        sys.stdout.write("\n--------reading %s--------\n"%fileinput.filename())
    sys.stdout.write("total:%d\t%s   %s" %(fileinput.lineno(),fileinput.filelineno(), line))
