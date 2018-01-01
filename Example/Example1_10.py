class A (object):
    def a(self):
        pass
    def b(self):
        pass


class B(A):
    def c(self):
        pass
    def d(self):
        pass

def get_member(cls, members = None):
    #get a list of all class members, ordered by class
    if members is None:
        members = []
    for k in cls.__bases__:
        get_member(k, members)
    for m in dir(cls):
        if m not in members:
            members.append(m)
    return members


print get_member(A)
print get_member(B)
print get_member(IOError)