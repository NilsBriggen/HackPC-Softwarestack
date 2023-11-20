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
            line = line.replace("\n", "")
            if line.startswith("//"):
                line = ""
            if "//" in line:
                line = line.split("//")[0]
            for escapeChar in escape_characters:
                line = line.replace(escapeChar, "")

            file[i] = line.upper()
        originalFile = file
        file = [x for x in file if x]
        self.file = file
        self.originalFile = originalFile
    
    def hasMoreLines(self):
        return self.linePointer < len(self.file)
    
    def advance(self):
        self.linePointer += 1

    def command_type(self):
        line = self.file[self.linePointer]
        if line.startswith("PUSH"):
            return "PUSH"
        elif line.startswith("POP"):
            return "POP"
        elif line in arithmetic_commands:
            return "ARITHMETIC"
        else:
            return "ERROR"
    
    def arg1(self):
        line = self.file[self.linePointer]
        return line if self.command_type() == "ARITHMETIC" else line.split(" ")[1]
    
    def arg2(self):
        line = self.file[self.linePointer]
        return line.split(" ")[2]
            
