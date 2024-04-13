import unittest
from get_domain import *

class TestLesserOfTwoEvens(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(get_domain("john.doe@example.com"), "example.com")
        self.assertEqual(get_domain("alice.smith@gmail.com"), "gmail.com")
        self.assertEqual(get_domain("info@company.org"), "company.org")

    def test_invalid_email(self):
        with self.assertRaises(Exception) as context:
            get_domain("invalid_email")

        self.assertTrue("Endereço de e-mail inválido. Deve conter exatamente um '@'." in str(context.exception))

    def test_empty_email(self):
        with self.assertRaises(Exception) as context:
            get_domain("")

        self.assertTrue("Endereço de e-mail inválido. Deve conter exatamente um '@'." in str(context.exception))

if __name__ == '__main__':
    unittest.main()
