"""unit test translator"""
import unittest

from translator import englishToFrench, frenchToEnglish


class TestEnglishTransaltor(unittest.TestCase):
    """
        TestEnglishTransaltor
    """
    def test_empty_english_text(self):
        """
            verify null input
        """
        self.assertEqual(englishToFrench(''),'')

    def test_hello_english_text(self):
        """
            verify Hello input
        """
        self.assertEqual(englishToFrench('Hello'),'Bonjour')


class TestFrenchTransaltor(unittest.TestCase):
    """
        TestFrenchTransaltor
    """
    def test_empty_french_text(self):
        """
            verify null input
        """
        self.assertEqual(frenchToEnglish(''),'')

    def test_hello_french_text(self):
        """
            verify Bonjour input
        """
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

if __name__ == '__main__':

    unittest.main()
