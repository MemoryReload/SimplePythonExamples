from sys import argv

script, filename =argv

print "We're going to erase %r." % filename,
condition = raw_input("Press 'N' to quit, any key to continue: ")
if condition=="N":
    exit()

print "Opening the file..."
target = open(filename,"r+")

#"w", or "w+" mode will both truncate the file from tell() returning position to the max position.
print "Truncating the file. Goodbye!"
target.truncate()

line_nums = 3
txt = ""
print "Now I'm going to ask you for %d lines." % line_nums
for i in range(1,line_nums+1):
    prompt = "line %d:"%i
    txt+=raw_input(prompt)
    if i!=line_nums:
        txt+="\n"

print "I'm going to write these to the file."

target.write(txt)

print "And finally, we close it."
target.close()