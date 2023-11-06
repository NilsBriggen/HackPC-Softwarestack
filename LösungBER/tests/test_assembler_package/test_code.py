'''
Created on July 2023

@author: reto.berger
'''

import unittest
from assembler_package import code


class TestCode(unittest.TestCase):
    
    def setUp(self):
        self.myC = code.Code()
        
    def tearDown(self):
        pass

    def test_compFieldTranslation(self):
        self.assertEqual(self.myC.comp('0'),'0101010')
        self.assertEqual(self.myC.comp('1'),'0111111')
        self.assertEqual(self.myC.comp('-1'),'0111010')
        self.assertEqual(self.myC.comp('D'),'0001100')
        self.assertEqual(self.myC.comp('D'),'0001100')
        self.assertEqual(self.myC.comp('A'),'0110000')
        self.assertEqual(self.myC.comp('M'),'1110000')
        self.assertEqual(self.myC.comp('!D'),'0001101')
        self.assertEqual(self.myC.comp('!A'),'0110001')
        self.assertEqual(self.myC.comp('!M'),'1110001')
        self.assertEqual(self.myC.comp('-D'),'0001111')
        self.assertEqual(self.myC.comp('-A'),'0110011')
        self.assertEqual(self.myC.comp('-M'),'1110011')
        self.assertEqual(self.myC.comp('D+1'),'0011111')
        self.assertEqual(self.myC.comp('A+1'),'0110111')
        self.assertEqual(self.myC.comp('M+1'),'1110111')
        self.assertEqual(self.myC.comp('D-1'),'0001110')
        self.assertEqual(self.myC.comp('A-1'),'0110010')
        self.assertEqual(self.myC.comp('M-1'),'1110010')
        self.assertEqual(self.myC.comp('D+A'),'0000010')
        self.assertEqual(self.myC.comp('D+M'),'1000010')
        self.assertEqual(self.myC.comp('D-A'),'0010011')
        self.assertEqual(self.myC.comp('D-M'),'1010011')
        self.assertEqual(self.myC.comp('A-D'),'0000111')
        self.assertEqual(self.myC.comp('M-D'),'1000111')
        self.assertEqual(self.myC.comp('D&A'),'0000000')
        self.assertEqual(self.myC.comp('D&M'),'1000000')
        self.assertEqual(self.myC.comp('D|A'),'0010101')
        self.assertEqual(self.myC.comp('D|M'),'1010101')
    
    def test_destFieldTranslation(self):
        self.assertEqual(self.myC.dest('0'),'000')
        self.assertEqual(self.myC.dest('M'),'001')
        self.assertEqual(self.myC.dest('D'),'010')
        self.assertEqual(self.myC.dest('MD'),'011')
        self.assertEqual(self.myC.dest('A'),'100')
        self.assertEqual(self.myC.dest('AM'),'101')
        self.assertEqual(self.myC.dest('AD'),'110')
        self.assertEqual(self.myC.dest('AMD'),'111')
    
    def test_jumpFieldTranslation(self):
        self.assertEqual(self.myC.jump('0'),'000')
        self.assertEqual(self.myC.jump('JGT'),'001')
        self.assertEqual(self.myC.jump('JEQ'),'010')
        self.assertEqual(self.myC.jump('JGE'),'011')
        self.assertEqual(self.myC.jump('JLT'),'100')
        self.assertEqual(self.myC.jump('JNE'),'101')
        self.assertEqual(self.myC.jump('JLE'),'110')
        self.assertEqual(self.myC.jump('JMP'),'111')
        
    def test_notEx(self):
        self.assertEqual(self.myC.jump('reto'), '000')


if __name__ == "__main__":
    unittest.main()
    