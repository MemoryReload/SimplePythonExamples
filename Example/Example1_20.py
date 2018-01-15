NAME = "script.py"
# BODY = """
# prnt 'owl-stretching time'
# """
BODY = """
print 'the ant, an introduction'
"""

try:
    code = compile(BODY, NAME, 'exec')
except SyntaxError, v:
    print "syntac error:", v, "in", NAME

print  code
exec code