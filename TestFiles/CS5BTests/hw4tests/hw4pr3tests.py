import unittest
import hw4pr3 as hw

class CompressLengthTest(unittest.TestCase):
  def testCompressLength1(self):
    studentCompress = hw.compress('1'*63 + '0')
    self.assertTrue(len(studentCompress) < len('1'*63 + '0'))
  def testCompressLength2(self):
    studentCompress = hw.compress(('1'*17 + '0'*15)*2)
    self.assertTrue(len(studentCompress) < len(('1'*17 + '0'*15)*2))

class CompressUncompressTest(unittest.TestCase):
  def testBoth1(self):
    studentCompress = hw.compress('1'*63 + '0')
    studentAnswer = hw.uncompress(studentCompress)
    self.assertEqual(studentAnswer,'1'*63 + '0')
  def testBoth2(self):
    studentCompress = hw.compress(('1'*17 + '0'*15)*2)
    studentAnswer = hw.uncompress(studentCompress)
    self.assertEqual(studentAnswer,('1'*17 + '0'*15)*2)

if __name__ == "__main__":
    unittest.main()
