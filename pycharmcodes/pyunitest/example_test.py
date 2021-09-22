import unittest

class Testexample(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('andre'.upper(), "ANDRE")

    def test_isupper(self):
        self.assertTrue('ANDRE'.isupper())
        self.assertFalse('andre'.isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ['hello', 'world'])

if __name__=='__main__':
    unittest.main()
