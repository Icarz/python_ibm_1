import unittest
from sample1 import add 

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4,7),11)
        self.assertEqual(add(4,8),12)
        self.assertNotEqual(add(4,9),14)


if __name__ == '__main__':
    unittest.main()