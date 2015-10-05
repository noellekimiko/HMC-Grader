import reverseTranslation as hw

import unittest

class ReverseTest(unittest.TestCase):
  def testReverse1(self):
    temp = sorted(hw.reverse({"a":"1","b":"2","c":"3","d":"3"}).items());
    self.assertTrue((temp == [('1', 'a'), ('2', 'b'), ('3', 'c or d')]) or (temp == [('1', 'a'), ('2', 'b'), ('3', 'd or c')]), temp)

  def testReverse2(self):
    temp2 = sorted(hw.reverse({'dude!' : 'hello', 'later' : 'goodbye', 'stoked' : 'happy', 'ciao' : 'goodbye'}).items()); 
    self.assertTrue((temp2 == [('goodbye', 'ciao or later'), ('happy', 'stoked'), ('hello', 'dude!')]) or (temp2 == [('goodbye', 'later or ciao'), ('happy', 'stoked'), ('hello', 'dude!')]), temp2)

  def testReverse3(self):
    self.assertEqual(sorted(hw.reverse({"*":45,"&":13,"-":9}).items()), [(9, '-'), (13, '&'), (45, '*')])

    
if __name__ == '__main__':
    unittest.main()