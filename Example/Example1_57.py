import  re

text = "you're no fun anymore..."

#literal replace
print re.sub("fun", "entertaining", text)

#colapse all non-letter sequences to a single dash
print re.sub("[^\w]+]", "-", text)

#convert all words to beeps
print  re.sub("\S+", "-BEEP-", text)