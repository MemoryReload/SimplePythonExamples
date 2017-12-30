class LazyImport(object):

    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None
        self.__length__ = 10

    def __getattr__(self, item):
        if self.module is None:
            self.module = __import__(self.module_name)
            print 'lazy load module %r success!' % self.module
        return getattr(self.module, item)

    @property
    def length(self):
        return self.__length__


squareRoot = LazyImport('squareRoot')
print squareRoot.length
print "the square root of 5 is %r" % squareRoot.sqrt(5, 0.0000001)
