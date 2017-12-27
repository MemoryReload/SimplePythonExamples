import glob, os

module=None
for file in glob.iglob("*Root.py"):
    print "file: %s" % file
    try:
        module_name, ext = os.path.splitext(os.path.basename(file))
        module = __import__(module_name)
        break
    except ImportError:
        pass

sqrt=module.sqrt(2,0.0000001)
print "the sqrt of 2 is %f" % sqrt