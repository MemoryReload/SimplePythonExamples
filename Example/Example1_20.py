NAME = "script.py"
BODY = """
prnt 'owl-stretching time'
"""

try:
    compile(BODY, NAME, 'exec')
except SyntaxError, v:
    print "syntac error:", v, "in", NAME