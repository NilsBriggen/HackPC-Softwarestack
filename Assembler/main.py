from codeTable import Translate
from file_parser import Parser
from symbolTable import Table
from hex import convert

# Opening Files
filePathInput = input("Path to source .asm file: ")

try:
    open(filePathInput, "r")
except Exception:
    print("Error: File not found!")
    exit()

filePath, _ = filePathInput.split(".asm")
filePathOutput = f"{filePath}.hack"
filePathHex = f"{filePath}.hex"

try:
    Output = open(filePathOutput, "w")
except Exception:
    Output = open(filePathOutput, "wx")

# Initialisation
tempOutput = []

table = Table()
translate = Translate()
parser = Parser()

parser.constructor(filePathInput)

# First iteration
while parser.hasMoreLines():
    category = parser.instructionType()
    if category == "L" and not table.contains(parser.symbol()):
        table.addEntry(parser.symbol(), None)
    parser.advance()

parser.linePointer = 0

# Second iteration
while parser.hasMoreLines():
    category = parser.instructionType()
    if category in ["A", "L"]:
        try:
            if parser.checkValue():
                address = "{0:016b}".format(int(parser.symbol()))
            else:
                if parser.symbol() not in table.symbolTable.keys():
                    table.addEntry(parser.symbol(), None)
                address = table.getAddress(parser.symbol())
                address = "{0:016b}".format(int(address))
            Output.write(address + "\n")
        except Exception:
            number, line = parser.findError()
            print(f"Error: Could not process line {str(number)} containing: {line}")
            exit()
    else:
        dest = translate.dest(parser.dest())
        comp = translate.comp(parser.comp())
        jump = translate.jump(parser.jump())

        if "error" in [dest, comp, jump]:
            number, line = parser.findError()
            print(f"Error: Could not process line {str(number)} containing: {line}")
            exit()

        command = f"111{comp}{dest}{jump}"

        Output.write(command + "\n")
    parser.advance()

Output.close()

with open(filePathOutput, "r") as bin:
    try:
        hex = open(filePathHex, "w")
    except Exception:
        hex = open(filePathHex, "wx")

    hex.write(convert(bin))

hex.close()

print(table.symbolTable)

print("File converted!")
