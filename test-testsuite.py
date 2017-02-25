import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

f __name__ == '__main__':
    unittest.main()