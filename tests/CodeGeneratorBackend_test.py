from nose.tools import *
from Example.Example1_22 import *


def test_compile():
    cg = CodeGeneratorBackend("<script>")
    cg.write("for i  in xrange(5):")
    cg.indent()
    cg.write("print 'code generation made easy!'")
    cg.dedent()
    assert_is_not_none(cg.end(), 'compile success')


def test_syntax():
    cg = CodeGeneratorBackend("<script>")
    cg.write("for i  in xrange(5)")
    cg.indent()
    cg.write("print 'code generation made easy!'")
    cg.dedent()
    with assert_raises(SyntaxError):
        cg.end()


def test_indent():
    cg = CodeGeneratorBackend("<script>")
    assert_raises(SyntaxError, CodeGeneratorBackend.dedent, cg)
