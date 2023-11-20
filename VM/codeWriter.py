class CodeWriter:
    def __init__(self, outputFileName):
        self.outputFile = open(outputFileName, "w")
        self.conversion = {
            "SP": "0",
            "LCL": "1",
            "ARG": "2",
            "THIS": "3",
            "THAT": "4",
            "TEMP": "5",
            "R": "13",
            "STATIC": "16",
        }
        self.outputFile.write("// Initialise SP\n@0\nD=A\n@SP\nM=D\n")
        self.comments = True
        
    def _generateComments(self, command, segment="", index=""):
        if self.comments:
            self.outputFile.write(f"\n// {command} {segment} {index}\n")
        
    def _writePush(self, segment, index):
        if segment == "POINTER":
            if index == "1":
                self.outputFile.write(f"@THAT\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            else:
                self.outputFile.write(f"@THIS\nA=M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
                
        if segment == "CONSTANT":
            self.outputFile.write(f"@{str(index)}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
        else:
            self.outputFile.write(f"@{segment}\nD=M\n@{index}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            
    def _writePop(self, segment, index):
        self.outputFile.write(f"@{segment}\nD=M\n@{index}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nM=D")

    def writePushPop(self, command, segment, index):
        self._generateComments(command, segment, index)
        if command == "PUSH":
            self._writePush(segment, index) 

        elif command == "POP":
            self._writePop(segment, index)
    
    def writeArithmetic(self, command):
        if command == "ADD":
            self.outputFile.write("@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n")
        elif command == "SUB":
            self.outputFile.write("@SP\nAM=M-1\nD=M\nA=A-1\nM=D-M\n")
        elif command == "NEG":
            self.outputFile.write("@SP\nAM=M-1\nD=M\n@0\nD=A-D\nM=D\n")
        elif command == "EQ":
            self.outputFile.write("@SP\nAM=M-1\nD=M\nA=A-1\nM=D-M\n@TRUE\nD;JEQ\n@SP\nA=M-1\nM=0\n@END_LABEL\n0;JMP\n(TRUE_LABEL)\n@SP\nA=M-1\nM=-1\n(END_LABEL)\n")
        elif command == "GT":
            self.outputFile.write("@SP\nAM=M-1\nD=M\nA=A-1\nM=D-M\n@TRUE\nD;JGT\n@SP\nA=M-1\nM=0\n@END_LABEL\n0;JMP\n(TRUE_LABEL)\n@SP\nA=M-1\nM=-1\n(END_LABEL)\n")
        elif command == "LT":
            self.outputFile.write("@SP\nAM=M-1\nD=M\nA=A-1\nM=D-M\n@TRUE\nD;JLT\n@SP\nA=M-1\nM=0\n@END_LABEL\n0;JMP\n(TRUE_LABEL)\n@SP\nA=M-1\nM=-1\n(END_LABEL)\n")
        elif command == "AND":
            self.outputFile.write("@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n")
        elif command == "OR":
            self.outputFile.write("@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n")
        elif command == "NOT":
            self.outputFile.write("@SP\nAM=M-1\nM=!M\n")
            
    def finish(self):
        self.outputFile.close()
            
            
            
            
            
            