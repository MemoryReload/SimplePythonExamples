class Rectangle(object):
    def __init__(self, color='white', width=10, height=10):
        super(Rectangle,self).__init__()
        print 'create a %s\t%r,sized:%d\theight:%d' %(color,self,width,height)


class RoundedRectangle(Rectangle):
    def __init__(self,*k,**kw):
        k=(self,)+k
        apply(Rectangle.__init__,k,kw)
        # super(RoundedRectangle,self).__init__(*k,**kw)


rect = Rectangle(color='green', width=100, height=100)
rect = RoundedRectangle(color='green', width=100, height=100)
rect = Rectangle(*('red',30,30))
rect = RoundedRectangle(*('red',30,30))
rect = Rectangle(**{ 'color' : 'blue', 'width' : 20, 'height' : 40})
rect = RoundedRectangle(**{ 'color' : 'blue', 'width' : 20, 'height' : 40})