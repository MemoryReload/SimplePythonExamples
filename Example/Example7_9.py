import asyncore
import string, socket
import StringIO
import mimetools, urlparse

class AsyncHTTP(asyncore.dispatcher_with_send):
# HTTP requester
    def __init__(self, uri, consumer):
        asyncore.dispatcher_with_send.__init__(self)
        self.uri = uri
        self.consumer = consumer
        #turn the uri into a valid request
        scheme, host, path, params, query, fragment = urlparse.urlparse(uri)
        assert  scheme == "http", "only surpports HTTP requests"
        try:
            host, port = string.split(host,":",1)
            port = int(port)
        except (TypeError, ValueError):
            port = 80 #default port
        if not path:
            path = "/"
        if params:
            path = path + ";" + params
        if query:
            path = path + "?" + query
        if fragment:
            path = path + "#" + fragment
        self.request = "GET %s HTTP/1.0\r\nHost: %s\r\n\r\n"%(path,host)
        self.host = host
        self.port = port
        self.status = None
        self.header = None
        self.data = ""
        #get things going!
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host,port))


    def handle_connect(self):
        #connection succeeded, send your fucking request
        self.send(self.request)

    def handle_expt(self):
        #connection failed; notify consumer (status is None)
        self.close()
        try:
            http_header = self.consumer.http_header
        except AttributeError:
            pass
        else:
            http_header(self)

    def handle_read(self):
        data = self.recv(2048)
        if not self.header:
            self.data = self.data + data
            try:
                i = string.index(self.data, "\r\n\r\n")
            except ValueError:
                return  #continue recieve data
            else:
                #parse header
                fp = StringIO.StringIO(self.data[:i+4])
                status = fp.readline()
                self.status = string.split(status," ",2)
                #followed by a rfc 822-style message header
                self.header = mimetools.Message(fp)
                #followed by a newline, and the payload (if any)
                data = self.data[i+4:]
                self.data = ""
                #notify consumer (status in non-zero)
                try:
                    http_header = self.consumer.http_header
                except AttributeError:
                    pass
                else:
                    http_header(self)
                if not self.connected:
                    return #channel was closed by consumer
        self.consumer.feed(data)

    def handle_close(self):
        self.consumer.close()
        self.close()


class DummyConsumer(object):
    def __init__(self):
        object.__init__(self)
        self.data = ""

    def http_header(self, request):
        #handle header
        if request.status is None:
            print "connection failed"
        else:
            print "status", "=>", request.status
            for key, value in request.header.items():
                print key, "=>", value

    def feed(self, data):
        #handle incoming data
        self.data = self.data + data

    def close(self):
        #end of data
        print self.data


if __name__ == "__main__":
    http_consumer = DummyConsumer()
    AsyncHTTP("http://www.baidu.com",http_consumer)
    asyncore.loop()



