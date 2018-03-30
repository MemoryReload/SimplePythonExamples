import asyncore, socket, time

#reference time
TIME1970 = 2208988800L

class TimeChannel(asyncore.dispatcher):
    def handle_write(self):
        t= int(time.time())+TIME1970
        t= chr(t>>24&255)+chr(t>>16&255)+chr(t>>8&255)+chr(t&255)
        self.send(t)
        self.close()

class TimeServer(asyncore.dispatcher):
    def __init__(self,port=37):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.bind(("",port))
        self.listen(5)
        print "Time server start listening on port ", port

    def writable(self):
        return False

    def handle_accept(self):
        sock, address = self.accept()
        TimeChannel(sock)

if __name__ == "__main__":
    server = TimeServer(8037)
    asyncore.loop()


