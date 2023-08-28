escape_characters = ["\n", "\t", "\r", "\v", "\f", "\b", "\a", "\0", "'", '"', "\\"]


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

    def hasMoreLines(self):
        return self.linePointer < len(self.file)

    def advance(self):
        self.linePointer += 1

    def instructionType(self):
        if self.file[self.linePointer].startswith("@"):
            return "A"
        elif self.file[self.linePointer].startswith("("):
            return "L"
        else:
            return "C"

    def symbol(self):
        line = self.file[self.linePointer]
        return (
            line.replace("(", "").replace(")", "")
            if line.startswith("(")
            else line.replace("@", "")
        )

    def dest(self):
        try:
            var, _ = self.file[self.linePointer].split("=")
        except:
            var = ""
        return var

    def comp(self):
        checker1, checker2 = False, False
        try:
            var, _ = self.file[self.linePointer].split(";")
        except:
            checker1 = True
        try:
            _, var = self.file[self.linePointer].split("=")
        except:
            checker2 = True
        if checker1 and checker2:
            var = ""
        return var  # type:ignore

    def jump(self):
        try:
            _, var = self.file[self.linePointer].split(";")
        except:
            var = ""
        return var

    def findError(self):
        errorLine = self.originalFile.index(self.file[self.linePointer]) + 1
        return errorLine, self.file[self.linePointer]

    def checkValue(self):
        if self.symbol().isdigit() and self.instructionType() == "A":
            self.advance()
            if self.comp() == "A":
                self.linePointer -= 1
                return True
            else:
                self.linePointer -= 1
        return False
