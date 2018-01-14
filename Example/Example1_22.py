import sys, string

class CodeGeneratorBackend(object):

    def __init__(self, filename = '<code>',tab = '\t'):
        # type: (str, str) -> CodeGeneratorBackend
        super(CodeGeneratorBackend,self).__init__()
        self.code = []
        self.filename = filename
        self.tab = tab
        self.level = 0

    def end(self):
        self.code.append("")
        return compile(string.join(self.code,"\n"), self.filename, "exec")


    def write(self, line):
        self.code.append(self.tab*self.level+line)


    def indent(self):
        self.level += 1


    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level -= 1


if __name__ == "__main__":
    c = CodeGeneratorBackend("<script>")
    c.write("for i  in xrange(5):")
    c.indent()
    c.write("print 'code generation made easy!'")
    c.dedent()
    code = c.end()
    exec code
