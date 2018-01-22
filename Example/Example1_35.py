import os

program = "python"
arguments = ["Example1_11.py"]

print os.execvp(program, (program,)+tuple(arguments))

#this code will never execute,because the execvp replaced the current process to do new job and never return
"""as the docuemtn said, These exec* functions all execute a new program, 
replacing the current process, and the current process is replaced immediately; 
they do not return. On Unix, the new executable is loaded into the current process, 
and will have the same process id as the caller. 
Errors will be reported as OSError exceptions."""

print "goodbye"