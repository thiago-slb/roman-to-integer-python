import unittest

from script import romanToInt

class TestMain(unittest.TestCase):

    def test_romanToInt1(self):
        s = romanToInt("III")
        self.assertEqual(s, 3)
        
    def test_romanToInt2(self):
        s = romanToInt("LVIII")
        self.assertEqual(s, 58)

    def test_romanToInt3(self):
        s = romanToInt("MCMXCIV")
        self.assertEqual(s, 1994)

if __name__ == '__main__':
    unittest.main()