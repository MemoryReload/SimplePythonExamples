import traceback
import sys

def function():
    raise IOError, "an I/O error occurred"

try:
    function()
except:
    """
    This is a shorthand for print_exception(sys.exc_type, sys.exc_value, sys.exc_traceback, limit, file). 
    (In fact, it uses sys.exc_info() to retrieve the same information in a thread-safe way instead of using
    the deprecated variables.)
    """
    traceback.print_exc()
    """
    This function returns a tuple of three values that give information about the exception that is currently 
    being handled. The information returned is specific both to the current thread and to the current stack frame. 
    If the current stack frame is not handling an exception, the information is taken from the calling stack frame, 
    or its caller, and so on until a stack frame is found that is handling an exception. Here, “handling an exception” 
    is defined as “executing or having executed an except clause.” For any stack frame, only information about the most 
    recently handled exception is accessible.

    If no exception is being handled anywhere on the stack, a tuple containing three None values is returned.
    Otherwise, the values returned are (type, value, traceback). Their meaning is: type gets the exception type
    of the exception being handled (a class object); value gets the exception parameter (its associated value or 
    the second argument to raise, which is always a class instance if the exception type is a class object); 
    traceback gets a traceback object (see the Reference Manual) which encapsulates the call stack at the point 
    where the exception originally occurred.

    If exc_clear() is called, this function will return three None values until either another exception is raised
    in the current thread or the execution stack returns to a frame where another exception is being handled.
    """
    info = sys.exc_info()
    print "** %s: %s" % info[:2]
    """
    Return a list of up to limit “pre-processed” stack trace entries extracted from the traceback object tb.
    It is useful for alternate formatting of stack traces. If limit is omitted or None, all entries are extracted.
    A “pre-processed” stack trace entry is a 4-tuple (filename, line number, function name*, text) representing the
    information that is usually printed for a stack trace. The text is a string with leading and trailing whitespace
    stripped; if the source is not available it is None.
    """
    for file, lineno, func, text in traceback.extract_tb(info[2]):
        print file, "line", lineno, "in", func, "=>", repr(text)
