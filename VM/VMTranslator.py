import parser_1, codeWriter

p = parser_1.Parser()
c = codeWriter.CodeWriter("Test.txt")

p.constructor("BasicTest.txt")

while p.hasMoreLines():
    if p.command_type() in ["PUSH", "POP"]:
        c.writePushPop(p.command_type(), p.arg1(), p.arg2())
    elif p.command_type() == "ARITHMETIC":
        c.writeArithmetic(p.arg1())
    p.advance()
    
c.finish()