import unittest
from find_word_in_phrase import *

class TestFindWordInPhrase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(find_word_in_phrase('dog', 'Is there a dog here?'))
        self.assertTrue(find_word_in_phrase('dog', 'Dog?'))
        self.assertTrue(find_word_in_phrase('dog', 'Dog...'))
        self.assertTrue(find_word_in_phrase('cat', 'Whose cat is this?'))
        
    def test_false(self):
        self.assertFalse(find_word_in_phrase('cat', 'Is there a dog here?'))
        self.assertFalse(find_word_in_phrase('cat', 'Dog?'))
        self.assertFalse(find_word_in_phrase('cat', 'Dog...'))
        self.assertFalse(find_word_in_phrase('dog', 'Whose cat is this?'))

if __name__ == '__main__':
    unittest.main()
