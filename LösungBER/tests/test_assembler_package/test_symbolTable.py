'''
Created on July 2023

@author: reto.berger
'''

import unittest
from assembler_package import symbolTable


class Test(unittest.TestCase):
    
    def setUp(self):
        self.myS = symbolTable.SymbolTable()
        
    def tearDown(self):
        pass

    def test_standardSymbols(self):
        self.assertTrue(self.myS.contains('R0'))
        self.assertEqual(self.myS.getAddress('R0'),0)
        self.assertTrue(self.myS.contains('R1'))
        self.assertEqual(self.myS.getAddress('R1'),1)
        self.assertTrue(self.myS.contains('R2'))
        self.assertEqual(self.myS.getAddress('R2'),2)
        self.assertTrue(self.myS.contains('R3'))
        self.assertEqual(self.myS.getAddress('R3'),3)
        self.assertTrue(self.myS.contains('R4'))
        self.assertEqual(self.myS.getAddress('R4'),4)
        self.assertTrue(self.myS.contains('R5'))
        self.assertEqual(self.myS.getAddress('R5'),5)
        self.assertTrue(self.myS.contains('R6'))
        self.assertEqual(self.myS.getAddress('R6'),6)
        self.assertTrue(self.myS.contains('R7'))
        self.assertEqual(self.myS.getAddress('R7'),7)
        self.assertTrue(self.myS.contains('R8'))
        self.assertEqual(self.myS.getAddress('R8'),8)
        self.assertTrue(self.myS.contains('R9'))
        self.assertEqual(self.myS.getAddress('R9'),9)
        self.assertTrue(self.myS.contains('R10'))
        self.assertEqual(self.myS.getAddress('R10'),10)
        self.assertTrue(self.myS.contains('R11'))
        self.assertEqual(self.myS.getAddress('R11'),11)
        self.assertTrue(self.myS.contains('R12'))
        self.assertEqual(self.myS.getAddress('R12'),12)
        self.assertTrue(self.myS.contains('R13'))
        self.assertEqual(self.myS.getAddress('R13'),13)
        self.assertTrue(self.myS.contains('R14'))
        self.assertEqual(self.myS.getAddress('R14'),14)
        self.assertTrue(self.myS.contains('R15'))
        self.assertEqual(self.myS.getAddress('R15'),15)
        self.assertTrue(self.myS.contains('SP'))
        self.assertEqual(self.myS.getAddress('SP'),0)
        self.assertTrue(self.myS.contains('LCL'))
        self.assertEqual(self.myS.getAddress('LCL'),1)
        self.assertTrue(self.myS.contains('ARG'))
        self.assertEqual(self.myS.getAddress('ARG'),2)
        self.assertTrue(self.myS.contains('THIS'))
        self.assertEqual(self.myS.getAddress('THIS'),3)
        self.assertTrue(self.myS.contains('THAT'))
        self.assertEqual(self.myS.getAddress('THAT'),4)
        self.assertTrue(self.myS.contains('SCREEN'))
        self.assertEqual(self.myS.getAddress('SCREEN'),16384)
        self.assertTrue(self.myS.contains('KBD'))
        self.assertEqual(self.myS.getAddress('KBD'),24576)
        
    def test_newSymbols(self):
        self.assertFalse(self.myS.contains('newVar'))
        self.myS.addEntry('newVar',1000)
        self.assertTrue(self.myS.contains('newVar'))
        self.assertEqual(self.myS.getAddress('newVar'),1000)
        self.assertNotEqual(self.myS.getAddress('newVar'),100)
        

if __name__ == "__main__":
    unittest.main()