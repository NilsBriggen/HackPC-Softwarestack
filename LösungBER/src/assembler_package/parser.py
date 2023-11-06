'''
Created on July 2023

@author: reto.berger
'''

class Parser():
    
    # Konstruktor
    def __init__(self, fileName):
        self.inputFile = open(fileName,'r')
        self.nextLine = ''
        self.currentCommand = ''
         
    def hasMoreLines(self):
        while True:
            self.nextLine = self.inputFile.readline().strip(' \t')
            if self.nextLine[:2] != '//' and len(self.nextLine) != 1:
                break
        if len(self.nextLine) != 0:
            return True 
        else:
            self.inputFile.close()
            return False 
    
    def advance(self):
        self.currentCommand = self._cleanCommand(self.nextLine)
    
    def instructionType(self):
        if self.currentCommand[0] == '@':
            return 'A_INSTRUCTION'
        elif self.currentCommand[0] == '(':
            return 'L_INSTRUCTION'
        else:
            return 'C_INSTRUCTION'
    
    def symbol(self):
        if self.instructionType() == 'A_INSTRUCTION':
            return self.currentCommand[1:]
        elif self.instructionType() == 'L_INSTRUCTION':
            return self.currentCommand.strip('()')
        else:
            return ''
    
    def dest(self):
        if self.instructionType() == 'C_INSTRUCTION': 
            if self.currentCommand.count('=') > 0:
                return self.currentCommand.split('=')[0]
            else:
                return 'null' 
        else:
            return ''
    
    def comp(self):
        if self.instructionType() == 'C_INSTRUCTION':
            if self.currentCommand.count('=') > 0:
                return self.currentCommand.split('=')[1] 
            else:
                return self.currentCommand.split(';')[0]
        else:
            return ''
    
    def jump(self):
        if self.instructionType() == 'C_INSTRUCTION': 
            if self.currentCommand.count(';') > 0:
                return self.currentCommand.split(';')[1]
            else:
                return 'null'
        else:
            return ''

    def _cleanCommand(self,strC):
        linePartition = strC.split('//')
        linePartition[0] = linePartition[0].replace(' ','')
        linePartition[0] = linePartition[0].replace('\t','')
        return linePartition[0].strip()
        