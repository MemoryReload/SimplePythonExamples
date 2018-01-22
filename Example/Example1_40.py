import os
import time

pid = os.fork()
# os.setpgrp()
if pid:
    print("the main process id is {}, gid is {}".format(os.getpid(), os.getgid()))
    os._exit(0)  # kill original process
print "daemon started, now change the gid of child process and let it become the leader process of a new group"
print("the child process id is {}, original gid is {}".format(os.getpid(), os.getgid()))
#success =  os.setpgrp()
#success = os.setpgid(0,0)
success = os.setpgid(0, os.getpid())
if success:
    print "get some problem here"
print("the child process id is {}, gid is {}".format(os.getpid(), os.getgid()))
time.sleep(10)
print "daemon terminated"
