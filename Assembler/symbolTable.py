class Table:
    def __init__(self):
        self.symbolTable = {
            "R0": "0",
            "R1": "1",
            "R2": "2",
            "R3": "3",
            "R4": "4",
            "R5": "5",
            "R6": "6",
            "R7": "7",
            "R8": "8",
            "R9": "9",
            "R10": "10",
            "R11": "11",
            "R12": "12",
            "R13": "13",
            "R14": "14",
            "R15": "15",
        }
        self.Indexer = 16

    def addEntry(self, symbol, address):
        if address != None:
            self.symbolTable[symbol] = str(address)
        else:
            self.symbolTable[symbol] = str(self.Indexer)
            self.Indexer += 1

    def contains(self, symbol):
        return symbol in self.symbolTable.keys()

    def getAddress(self, symbol):
        return self.symbolTable[symbol]
