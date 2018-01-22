import os

def run(program, *args):
    pid = os.fork();
    if not pid:
        os.execvp(program, (program,)+args)
    #stat is a tuple which contains two items. The first is the pid of a child procrss, The seconde is exit status.
    stat = os.wait()
    return stat[1]

run("python", "Example1_11.py")

print "goodbye"