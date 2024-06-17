
# Imports
import unittest
from filter_out import *

# Test definitions
class TestCountWordInPhrase(unittest.TestCase):
    def test_equal(self):

        words = ['soup','dog','salad','cat','great']

        self.assertEqual(filter_out(words, 's'), ['soup','salad'])
        self.assertEqual(filter_out(words, 'd'), ['dog'])
        self.assertEqual(filter_out(words, 'c'), ['cat'])

# Main
if __name__ == '__main__':
    unittest.main()
