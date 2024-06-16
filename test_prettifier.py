import unittest
from prettifier import NumberPrettifier  

class TestNumberPrettifier(unittest.TestCase):
    def test_thousands(self):
        self.assertEqual(NumberPrettifier.prettify(1000), "1K")
        self.assertEqual(NumberPrettifier.prettify(1234), "1.2K")
        self.assertEqual(NumberPrettifier.prettify(999), "999")
        self.assertEqual(NumberPrettifier.prettify(10000), "10K")

    def test_millions(self):
        self.assertEqual(NumberPrettifier.prettify(1000000), "1M")
        self.assertEqual(NumberPrettifier.prettify(2500000.34), "2.5M")
    
    def test_billions(self):
        self.assertEqual(NumberPrettifier.prettify(1000000000), "1B")
        self.assertEqual(NumberPrettifier.prettify(1123456789), "1.1B")
    
    def test_trillions(self):
        self.assertEqual(NumberPrettifier.prettify(1000000000000), "1T")
        self.assertEqual(NumberPrettifier.prettify(2000000000000.55), "2T")
    
    def test_small_numbers(self):
        self.assertEqual(NumberPrettifier.prettify(532), "532")
        self.assertEqual(NumberPrettifier.prettify(532.123), "532.123")
    
    def test_negative_numbers(self):
        self.assertEqual(NumberPrettifier.prettify(-2500000.34), "-2.5M")
        self.assertEqual(NumberPrettifier.prettify(-1123456789), "-1.1B")
        self.assertEqual(NumberPrettifier.prettify(-1000000000000), "-1T")

    def test_zero(self):
        self.assertEqual(NumberPrettifier.prettify(0), "0")

if __name__ == "__main__":
    unittest.main()
