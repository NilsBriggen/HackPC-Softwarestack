'''
Created on July 2023

@author: reto.berger
'''

import sys 
import code, symbolTable, parser

''' Beim Run-button unter 'Run configurations...' im Tab 
    Arguments den Pfad (oder den Namen) der asm Datei eingeben.
    Der Pfad kann mit Rechtsklick -> Properties ermittelt werden
'''

class Assembler():
    
    def __init__(self,pathAsm,pathHack):
        self.path_to_asmFile = pathAsm 
        self.path_to_hackFile = pathHack 
        self.symTbl = symbolTable.SymbolTable()
        self.myCode = code.Code()
        
    def firstPars(self):
        pars = parser.Parser(self.path_to_asmFile)
        currentLine = 0
        while pars.hasMoreLines():
            pars.advance()
            if pars.instructionType() == 'L_INSTRUCTION':
                self.symTbl.addEntry(pars.symbol(),currentLine) 
            else:
                currentLine += 1
                
    def secondPars(self):
        pars = parser.Parser(self.path_to_asmFile)
        newVarAdd = 16
        hackCode = ''
        while pars.hasMoreLines():
            pars.advance()
            if pars.instructionType() == 'A_INSTRUCTION':
                newLine, newVarAdd = self._getA_hack(pars.symbol(),newVarAdd)
                hackCode += newLine
            if pars.instructionType() == 'C_INSTRUCTION':
                newLine = self._getC_hack(pars.dest(),pars.comp(),pars.jump())
                hackCode += newLine
        with open(self.path_to_hackFile,'w') as newFile:
            newFile.write(hackCode)

        print(self.symTbl.table)
    
    def _getA_hack(self,symbol,newVarAdd):
        if symbol.isnumeric():
            newLine = int(symbol)
        elif self.symTbl.contains(symbol):
            newLine = self.symTbl.getAddress(symbol) 
        else:
            newLine = newVarAdd
            self.symTbl.addEntry(symbol,newVarAdd)
            newVarAdd += 1
        return (bin(newLine)[2:].zfill(16) + '\n', newVarAdd)
    
    def _getC_hack(self,dest,comp,jump):
        newLine = '111'
        newLine += self.myCode.comp(comp)
        newLine += self.myCode.dest(dest)
        newLine += self.myCode.jump(jump)
        return newLine + '\n'

if __name__ == '__main__':
    pathAsm = sys.argv[1]
    pathHack = sys.argv[1].replace('.asm','.hack')
    
    assembler = Assembler(pathAsm,pathHack)
    assembler.firstPars()
    assembler.secondPars()
    

