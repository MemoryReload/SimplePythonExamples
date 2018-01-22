import os
import time

pid = os.fork()
if pid:
    print("the main process euid is {}, gid is {}, id is {}, pgid is {}".format(os.geteuid(),os.getgid(), os.getpid(), os.getpgrp()))
    os._exit(0)  # kill original process
print("the child process euid is {}, gid is {}, id is {}, original pgid is {}".format(os.geteuid(),os.getgid(),os.getpid(), os.getpgrp()))
print "daemon started, now change the pgid of child process and let it become the leader process of a new group"
success =  os.setpgrp()
# success = os.setpgid(0, 0)
if success:
    print "get some problem here"
print("the child process euid is {}, gid is {}, id is {}, pgid is {}".format(os.geteuid(),os.getgid(),os.getpid(), os.getpgrp()))
time.sleep(10)
print "daemon terminated"
