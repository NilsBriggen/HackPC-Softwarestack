escape_characters = ["\n", "\t", "\r", "\v", "\f", "\b", "\a", "\0", "'", '"', "\\"]
arithmetic_commands = ["ADD", "SUB", "NEG", "EQ", "GT", "LT", "AND", "OR", "NOT"]

class Parser:
    def __init__(self):
        self.file = []
        self.originalFile = []
        self.linePointer = 0
        self.errorLine = 0

    def constructor(self, input_file):
        file = open(input_file, "r").readlines()
        for i in range(len(file)):
            line = file[i]
            line = line.replace(" ", "")
            line = line.replace("\n", "")
            if line.startswith("//"):
                line = ""
            if line.startswith("@") == False:
                line = line.upper()
            if "//" in line:
                line = line.split("//")[0]
            if "KEYBOARD" in line:
                line = line.replace("KEYBOARD", "KBD")
            for escapeChar in escape_characters:
                line = line.replace(escapeChar, "")

            file[i] = line
        originalFile = file
        file = [x for x in file if x]
        self.file = file
        self.originalFile = originalFile

    def advance(self):
        self.linePointer += 1
        return self.linePointer < len(self.file)
    
    def advance(self):
        self.linePointer += 1

    def command_type(self): # return values: C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL
        line = self.file[self.linePointer]
        if line.startswith("PUSH"):
            return "C_PUSH"
        elif line.startswith("POP"):
            return "C_POP"
        elif line.upper() in arithmetic_commands:
            return "C_ARITHMETIC"
        else:
            return "C_ERROR"
    
    def arg1(self):
        line = self.file[self.linePointer]
        return line if self.command_type() == "C_ARITHMETIC" else line.split(" ")[1]
    
    def arg2(self):
        line = self.file[self.linePointer]
        return line.split(" ")[2]
            
