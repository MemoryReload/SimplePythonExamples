import glob, os, sys


def get_name_with_path(pathname):
    paths = glob.glob(pathname)
    path = paths[0]
    name = None
    if path:
        name, ext = os.path.splitext(os.path.basename(path))
    return name



#load module
def get_module_with_name(name):
    module=None
    try:
        #this is the important
        module = __import__(name)
    except ImportError:
        pass
    return module

#load module content
def get_content_with_module_name(name, content_list=[]):
    content = None
    try:
        #this is the important
        content = __import__(name, globals(), locals(),content_list)
    except ImportError:
        pass
    return content

print 'cwd: %r' % os.getcwd()

# name = get_name_with_path('squareRoot.py')
# print "name: %s" % name
module = get_module_with_name('squareRoot')
print "the square root of 2 is %r" % module.sqrt(2,0.0000001)

# name = get_name_with_path('./ex')
# print "name: %s" % name

package = get_content_with_module_name('ex')
print 'package content is %r' % package

#if  the formlist not defined, package will be load
package = get_content_with_module_name('ex.ex4')
print 'package content is %r' % package

#if the formlist defined, the ex4 module will be load
module = get_content_with_module_name('ex.ex4',['anything'])
print 'module content is %r' % module

#reload the module
reload(module)

