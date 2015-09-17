import hw3pr3 as hw

import unittest

class FoldTest(unittest.TestCase):
    def testFold1(self):
        self.assertEqual(hw.fold("ACCCCCU"), 1)
    def testFold2(self):
        self.assertEqual(hw.fold("ACCCCGU"), 2)
    def testFold3(self):
        self.assertEqual(hw.fold("AAUUGCGC"), 4)
    def testFold4(self):
        self.assertEqual(hw.fold("ACUGAGCCCU"), 3)
    def testFold5(self):
        self.assertEqual(hw.fold("ACUGAGCCCUGUUAGCUAA"), 8)

class MFoldTest(unittest.TestCase):
    def testMFold1(self):
        testRNA = "GGAUACGGCCAUACUGCGCAGAAAGCACCGCUUCCCAUCCGAACAGCGAAGUUAAGCUGCGCCAGGCGGUGUUAGUACUGGGGUGGGCGACCACCCGGGAAUCCACCGUGCCGUAUCCU"
        self.assertEqual(hw.mfold(testRNA), 52)
    def testMFold2(self):
        self.assertEqual(hw.mfold("ACCCCCU"), 1)
    def testMFold3(self):
        self.assertEqual(hw.mfold("AAUUGCGC"), 4)
    def testMFold4(self):
        self.assertEqual(hw.mfold("ACUGAGCCCU"), 3)
    def testMFold5(self):
        self.assertEqual(hw.mfold("ACUGAGCCCUGUUAGCUAA"), 8)

#extra credit
class GetFoldTest(unittest.TestCase):
    def testGetFold1(self):
        testString = "ACCCCCU"
        result = hw.getFold(testString)
        self.assertEqual(result[0], 1)
        self.assertEqual(testString[result[1][0][0]], testString[result[1][0][1]])
    def testGetFold2(self):
        testString = "ACCCCGU"
        result = hw.getFold(testString)
        self.assertEqual(result[0], 2)
        self.assertEqual(testString[result[1][0][0]], testString[result[1][0][1]])
        self.assertEqual(testString[result[1][1][0]], testString[result[1][1][1]])
    def testGetFold3(self):
        testString = "AAUUGCGC"
        result = hw.getFold(testString)
        self.assertEqual(result[0], 4)
        self.assertEqual(testString[result[1][0][0]], testString[result[1][0][1]])
        self.assertEqual(testString[result[1][1][0]], testString[result[1][1][1]])
        self.assertEqual(testString[result[1][2][0]], testString[result[1][2][1]])
        self.assertEqual(testString[result[1][3][0]], testString[result[1][3][1]])
    def testGetFold4(self):
        testString = "ACUGAGCCCU"
        result = hw.getFold(testString)
        self.assertEqual(result[0], 3)
        self.assertEqual(testString[result[1][0][0]], testString[result[1][0][1]])
        self.assertEqual(testString[result[1][1][0]], testString[result[1][1][1]])
        self.assertEqual(testString[result[1][2][0]], testString[result[1][2][1]])
    def testGetFold5(self):
        testString = "ACUGAGCCCUGUUAGCUAA"
        result = hw.getFold(testString)
        self.assertEqual(result[0], 8)
        self.assertEqual(testString[result[1][0][0]], testString[result[1][0][1]])
        self.assertEqual(testString[result[1][1][0]], testString[result[1][1][1]])
        self.assertEqual(testString[result[1][2][0]], testString[result[1][2][1]])
        self.assertEqual(testString[result[1][3][0]], testString[result[1][3][1]])
        self.assertEqual(testString[result[1][4][0]], testString[result[1][4][1]])
        self.assertEqual(testString[result[1][5][0]], testString[result[1][5][1]])
        self.assertEqual(testString[result[1][6][0]], testString[result[1][6][1]])
        self.assertEqual(testString[result[1][7][0]], testString[result[1][7][1]])


if __name__ == '__main__':
    unittest.main()
