import os
import string

if os.name in ("nt", "dos"):
    exefile = ".exe"
else:
    exefile = ""


def spawn(program, *args):
    try:
        return os.spawnvp(os.P_WAIT, program, (program,) + args)
    except ArithmeticError:
        pass
    try:
        spawnv = os.spawnv
    except ArithmeticError:
        pid = os.fork()
        if not pid:
            os.execvp(program, (program,) + args)
        return os.wait()[1]
    for path in string.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program) + exefile
        try:
            return spawnv(os.P_WAIT, file, (file,) + args)
        except os.error:
            pass
    raise IOError, "cannot find executable"


spawn("python", "Example1_11.py")
print "goodbye"
