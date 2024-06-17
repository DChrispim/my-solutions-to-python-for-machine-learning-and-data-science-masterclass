
# Imports
import unittest
from caught_speeding import *

# Test definitions
class TestCountWordInPhrase(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(caught_speeding(10,False), 'No ticket')
        self.assertEqual(caught_speeding(81,True), 'Small Ticket')
        self.assertEqual(caught_speeding(81,False), 'Big Ticket')

# Main
if __name__ == '__main__':
    unittest.main()
