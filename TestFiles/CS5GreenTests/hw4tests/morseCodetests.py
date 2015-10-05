import morseCode as hw

import unittest

morsecode =  {'a': '.-' ,
              'b': '-...', 
              'c':'-.-.',
              'd':'-..',
              'e':'.',
              'f':'..-.',
              'g':'--.',  
              'h':'....',
              'i':'..',
              'j':'.---',
              'k':'-.-',
              'l':'.-..',
              'm':'--',
              'n':'-.',
              'o':'---',
              'p':'.--.',  
              'q':'--.-',
              'r':'.-.',
              's':'...',
              't':'-',
              'u':'..-',
              'v':'...-',
              'w':'.--',
              'x':'-..-',
              'y':'-.--',  
              'z':'--..'}

class MorseTest(unittest.TestCase):
  def testMorse1(self):
    self.assertEqual(hw.morse('a boy', morsecode), '.-   -... --- -.--')
  def testMorse2(self):
    self.assertEqual(hw.morse('a man a plan a canal panama', morsecode), '.-   -- .- -.   .-   .--. .-.. .- -.   .-   -.-. .- -. .- .-..   .--. .- -. .- -- .-')
  def testMorse3(self):
    self.assertEqual(hw.morse('i love ladas', morsecode), '..   .-.. --- ...- .   .-.. .- -.. .- ...')
  def testMorse4(self):
    self.assertEqual(hw.morse('zyzyzzus', morsecode), '--.. -.-- --.. -.-- --.. --.. ..- ...')
  def testMorse5(self):
    self.assertEqual(hw.morse('hmc', morsecode), '.... -- -.-.')


if __name__ == '__main__':
    unittest.main()