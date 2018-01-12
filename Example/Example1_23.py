from os import path

dir=path.dirname(__file__)
file=path.join(dir,"./../squareRoot.py")
print(file)
execfile(file)

def EXECFILE(filename, locals=None, globals=None):
    exec compile(open(filename).read(), filename, "exec") in locals, globals

print("----------------------------------")
EXECFILE(file)