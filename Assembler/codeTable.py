class Translate:
    def __init__(self):
        self.dest_dict = {
            "": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111",
        }
        self.jump_dict = {
            "": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }
        self.comp_dict = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "!D": "0001101",
            "!A": "0110001",
            "-D": "0001111",
            "-A": "0110011",
            "D+1": "0011111",
            "1+D": "0011111",
            "A+1": "0110111",
            "1+A": "0110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "D+A": "0000010",
            "A+D": "0000010",
            "D-A": "0010011",
            "A-D": "0000111",
            "D&A": "0000000",
            "A&D": "0000000",
            "D|A": "0010101",
            "A|D": "0010101",
            "M": "1110000",
            "!M": "1110001",
            "-M": "1110011",
            "M+1": "1110111",
            "1+M": "1110111",
            "M-1": "1110010",
            "D+M": "1000010",
            "M+D": "1000010",
            "D-M": "1010011",
            "M-D": "1000111",
            "D&M": "1000000",
            "M&D": "1000000",
            "D|M": "1010101",
            "M|D": "1010101",
        }

    def dest(self, input):
        try:
            return self.dest_dict[input]
        except:
            return "error"

    def jump(self, input):
        try:
            return self.jump_dict[input]
        except:
            return "error"

    def comp(self, input):
        try:
            return self.comp_dict[input]
        except:
            return "error"
