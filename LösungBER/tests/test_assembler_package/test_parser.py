'''
Created on July 2023

@author: reto.berger
'''
import unittest
from unittest.mock import mock_open, patch
from assembler_package import parser


class Test(unittest.TestCase):


    def setUp(self):
        fileASM = '''
        
        // Das ist ein Test ams Code
         
           A  =    M  +    1  //Mit einem Kommentar
                    ( newVar  )       
           @  oldVar
             D ;    JEQ    // wenn nicht, gehe zu oldVar  
                  
        
        '''
        self.mockedFileASM = mock_open(read_data=fileASM)

    def tearDown(self):
        pass
    
    def test_parserCommandLines(self):
        with patch('assembler_package.parser.open',self.mockedFileASM):
            myP = parser.Parser('fakePath/fakeFile.ams')
            self.mockedFileASM.assert_called_once_with('fakePath/fakeFile.ams','r')
            self.assertTrue(myP.hasMoreLines())
            myP.advance()
            self.assertTrue(myP.hasMoreLines())
            myP.advance()
            self.assertTrue(myP.hasMoreLines())
            myP.advance()
            self.assertTrue(myP.hasMoreLines())
            myP.advance()
            self.assertFalse(myP.hasMoreLines())
        
    def test_parserInstructions(self):
        with patch('assembler_package.parser.open',self.mockedFileASM):
            myP = parser.Parser('fakePath/fakeFile.ams')
            self.mockedFileASM.assert_called_once_with('fakePath/fakeFile.ams','r')
            if myP.hasMoreLines(): 
                myP.advance()
            self.assertEqual(myP.instructionType(),'C_INSTRUCTION')
            self.assertEqual(myP.currentCommand,'A=M+1')
            self.assertEqual(myP.symbol(),'')
            self.assertEqual(myP.dest(),'A')
            self.assertEqual(myP.comp(),'M+1')
            self.assertEqual(myP.jump(),'null')
            if myP.hasMoreLines(): 
                myP.advance()
            self.assertEqual(myP.instructionType(),'L_INSTRUCTION')
            self.assertEqual(myP.currentCommand,'(newVar)')
            self.assertEqual(myP.symbol(),'newVar')
            self.assertEqual(myP.dest(),'')
            self.assertEqual(myP.comp(),'')
            self.assertEqual(myP.jump(),'')
            if myP.hasMoreLines(): 
                myP.advance()
            self.assertEqual(myP.instructionType(),'A_INSTRUCTION')
            self.assertEqual(myP.currentCommand,'@oldVar')
            self.assertEqual(myP.symbol(),'oldVar')
            self.assertEqual(myP.dest(),'')
            self.assertEqual(myP.comp(),'')
            self.assertEqual(myP.jump(),'')
            if myP.hasMoreLines(): 
                myP.advance()
            self.assertEqual(myP.instructionType(),'C_INSTRUCTION')
            self.assertEqual(myP.currentCommand,'D;JEQ')
            self.assertEqual(myP.symbol(),'')
            self.assertEqual(myP.dest(),'null')
            self.assertEqual(myP.comp(),'D')
            self.assertEqual(myP.jump(),'JEQ')


if __name__ == "__main__":
    unittest.main()