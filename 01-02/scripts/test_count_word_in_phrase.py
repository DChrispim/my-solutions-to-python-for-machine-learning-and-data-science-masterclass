
# Imports
import unittest
from count_word_in_phrase import *

# Test definitions
class TestCountWordInPhrase(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(count_word_in_phrase('dog', 'Is there a dog here?'), 1)
        self.assertEqual(count_word_in_phrase('dog', 'Dog?'),1 )
        self.assertEqual(count_word_in_phrase('cat', 'Whose cat is this?'), 1)
        self.assertEqual(count_word_in_phrase('dog', 'This dog runs faster than the other dog dude!'),2)
        self.assertEqual(count_word_in_phrase('cat', 'This dog runs faster than the other dog dude!'),0)

# Main
if __name__ == '__main__':
    unittest.main()
