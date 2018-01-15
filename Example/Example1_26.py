class HTTPError(Exception):
    def __init__(self, url, errcode, errmsg):
        self.url = url
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        return "<HTTPError for %s: %s %s>" % (self.url, self.errcode, self.url)


try:
    raise HTTPError("http://www.baidu.com", "404", "Not found")
except HTTPError, error:
    print "url => %s" % error.url
    print "errcode => %s" % error.errcode
    print "errmsg => %s" % error.errmsg
    raise  # reraise exeption
