import poplib
import string, random
import StringIO, rfc822

SEVER = "pop.163.com"
USER = "heping_tsdwx@163.com"
PASSWD = ""

#connect to sever
server = poplib.POP3(SEVER)

#login
server.user(USER)
server.pass_(PASSWD)

#list items on server
resp, items, octets = server.list()

#print itmes
for item in items:
    print item
#let user choose
input = raw_input("the messgae index you want to read:")
id, size = string.split(items[int(input)-1])

#fetch the message
resp, text, octets = server.retr(id)

text = string.join(text,"\n")
file = StringIO.StringIO(text)

message = rfc822.Message(file)

for k, v in message.items():
    print k, "=", v
print "-"*120
print message.fp.read()