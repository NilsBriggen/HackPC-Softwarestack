class CodeWriter:
    def constructor(self, outputFileName):
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
        self.outputFile.write("@0\nD=A\n@SP\nM=D\n")

    def writePushPop(self, command, segment, index="0"):
        if command == "C_PUSH":
            if segment in ["LCL", "ARG", "THIS", "THAT"]:
                self.outputFile.write(f"@{index}\nD=A\n@{self.conversion[segment]}\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "constant":
                self.outputFile.write(f"@{index}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment in ["TEMP", "R", "STATIC"] :
                location = int(self.conversion[segment]) + int(index)
                self.outputFile.write(f"@{location}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")
            elif segment == "POINTER":
                if 
            # ... handle other segments like pointer, static

        elif command == "C_POP":
            if segment in ["local", "argument", "this", "that"]:
                self.outputFile.write(f"@{index}\nD=A\n@{self.conversion[segment]}\nD=D+M\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            elif segment == "temp":
                location = int(self.conversion[segment]) + int(index)
                self.outputFile.write(f"@SP\nAM=M-1\nD=M\n@{location}\nM=D\n")
            # ... handle other segments like pointer, static
