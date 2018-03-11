import sys, getopt

def help_descrition():
    print "This command is xxxxxxx"

help = False
verbose = False
file_type = "txt"
output = "./output.txt"

try:
    options, args = getopt.getopt(sys.argv[1:], "hvt:o:", ["help", "verbose", "output=", "type="])
except getopt.GetoptError, (error, message):
    print "Error code: "+error+" message: "+message
    help_descrition()
else:
    if not args:
        help_descrition()
        exit(0)
    for (opt, val) in options:
        if opt in ["-h", "--help"]:
            help_descrition()
            exit(0)
        elif opt in ["-v", "--verbose"]:
            verbose = True
        elif opt in ["-t", "--type"]:
            file_type = val
        elif opt in ["-o", "--output"]:
            output = val
        else:
            pass

    print "verbose: "+repr(verbose)
    print "file_type: "+file_type
    print "output_file: "+output
    print "input_file"+repr(args)







