#coding:utf-8
import code, sys


def keyboard(banner=None):
    try:
        raise None
    except:
        # frame = sys.exc_info()[2].tb_frame.f_back
        #获取到崩溃的栈追溯对象
        backtrace = sys.exc_info()[2]
        #获取当前崩溃的栈帧keyboard
        current_frame = backtrace.tb_frame
        #通过f_back回溯访问上一帧func
        frame=current_frame.f_back
    # evalueate commands in current namespace
    #获取func的全局环境变量
    namespace = frame.f_globals.copy()
    #获取func的局部变量
    namespace.update(frame.f_locals)
    #code对象装载环境变量，并以交互模式运行
    code.interact(banner=banner, local=namespace)

def func():
    print "START"
    a = 10
    # keyboard("Python 2.7.14 Interactive Interpretor")
    keyboard()
    print "END"

func()

