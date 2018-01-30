import re
import string

text = "a line of text \\012another line of text \\012etc..."
#can be also write like this
# text = r"a line of text \012another line of text \012etc..."

def octal(match):
    #replace octal code with corresponding ASCII character
    return  chr(string.atoi(match.group(1), 8))

octal_pattern = re.compile(r"\\(\d\d\d)")

print text

print octal_pattern.sub(octal, text)