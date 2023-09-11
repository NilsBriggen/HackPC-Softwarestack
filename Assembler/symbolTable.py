class Table:
    def __init__(self):
        self.Indexer = 1
        self.symbolTable = {
            "SP": "0",
            "LCL": "1",
            "ARG": "2",
            "THIS": "3",
            "THAT": "4",
            "KBD": "24576",
            "SCREEN": "16384",
        }

    def addEntry(self, symbol, address):
        if address != None:
            self.symbolTable[symbol] = address
        else:
            while self.Indexer in self.symbolTable.values():
                self.Indexer += 1
            self.symbolTable[symbol] = str(self.Indexer)
            self.Indexer += 1

    def contains(self, symbol):
        return symbol in self.symbolTable.keys()

    def getAddress(self, symbol):
        return self.symbolTable[symbol]
