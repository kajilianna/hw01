import unittest
from src.example import hello

class TestExample(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello from src!")

if __name__ == '__main__':
    unittest.main()