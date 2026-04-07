import unittest
def add( a, b):
    return a + b

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,4), 6)
        self.assertEqual(add(5,2), 7)


if __name__ == '__main__':
    unittest.main()