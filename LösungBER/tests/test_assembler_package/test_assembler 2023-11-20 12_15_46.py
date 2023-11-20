'''
Created on July 2023

@author: reto.berger
'''
import unittest
from unittest.mock import mock_open, patch
from assembler_package import assembler

class Test(unittest.TestCase):

    def test_FirstPars(self):
        fake_asmFile = '''
        D = M + 1   // Zeile 0
        (LOOP)      // Label auf nächste Zeile
        // Kommentar
        @i          // Zeile 1
        D = M       // Zeile 2
        @LOOP       // Zeile 3
        0;JMP       // Zeile 4
        // Kommentar
        (End)       // Label auf nächste Zeile
        @End        // Zeile 5
        0;JMP       // Zeile 6
        '''
        with patch('assembler_package.parser.open',mock_open(read_data=fake_asmFile)):
            myA = assembler.Assembler('fakePath/fake.asm','fakePath/fake.hack')
            myA.firstPars()
            self.assertFalse(myA.symTbl.contains('i'))
            self.assertTrue(myA.symTbl.contains('LOOP'))
            self.assertEqual(myA.symTbl.getAddress('LOOP'),1)
            self.assertTrue(myA.symTbl.contains('End'))
            self.assertEqual(myA.symTbl.getAddress('End'),5)
            
    def test_secondPars(self):
        fake_asmFile = '''@R1        // Zeile  0
                          D = M      // Zeile  1
                          @i         // Zeile  2
                          M = D      // Zeile  3
                          @product   // Zeile  4
                          M = 0      // Zeile  5
                          (LOOP)
                          @i         // Zeile  6
                          D = M      // Zeile  7
                          @END       // Zeile  8
                          D;JEQ      // Zeile  9
                          @R0        // Zeile 10
                          D = M      // Zeile 11
                          @product   // Zeile 12
                          M = D + M  // Zeile 13
                          @i         // Zeile 14
                          M = M - 1  // Zeile 15
                          @LOOP      // Zeile 16
                          0;JMP      // Zeile 17
                          (END)
                          @product   // Zeile 18
                          D = M      // Zeile 19
                          @R2        // Zeile 20
                          M = D      // Zeile 21
                          @END       // Zeile 22
                          0;JMP      // Zeile 23
        '''
        fake_hackFile = '''0000000000000001
                           1111110000010000
                           0000000000010000
                           1110001100001000
                           0000000000010001
                           1110101010001000
                           0000000000010000
                           1111110000010000
                           0000000000010010
                           1110001100000010
                           0000000000000000
                           1111110000010000
                           0000000000010001
                           1111000010001000
                           0000000000010000
                           1111110010001000
                           0000000000000110
                           1110101010000111
                           0000000000010001
                           1111110000010000
                           0000000000000010
                           1110001100001000
                           0000000000010010
                           1110101010000111
        '''
        with patch('assembler_package.parser.open',mock_open(read_data=fake_asmFile)):
            with patch('assembler_package.assembler.open',mock_open()) as mocked:
                myA = assembler.Assembler('fakePath/fake.asm','fakePath/fake.hack')
                myA.symTbl.addEntry('LOOP',6)
                myA.symTbl.addEntry('END',18)
                myA.secondPars()
            self.assertTrue(myA.symTbl.contains('i'))
            self.assertEqual(myA.symTbl.getAddress('i'),16)
            self.assertTrue(myA.symTbl.contains('product'))
            self.assertEqual(myA.symTbl.getAddress('product'),17)
            mocked().write.assert_called_once_with(fake_hackFile.replace(' ',''))
            

if __name__ == "__main__":
    unittest.main()