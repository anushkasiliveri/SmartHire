
import unittest

from src.data_processing.text_cleaner import clean_resume_text


class TestTextCleaner(unittest.TestCase):

    def test_lowercase_conversion(self):
        result = clean_resume_text("PYTHON DEVELOPER")
        self.assertEqual(result, "python developer")

    def test_email_removal(self):
        result = clean_resume_text("Contact: rahul@gmail.com")
        self.assertNotIn("rahul@gmail.com", result)

    def test_url_removal(self):
        result = clean_resume_text("Website: https://example.com")
        self.assertNotIn("https://example.com", result)

    def test_extra_spaces_removal(self):
        result = clean_resume_text("Python     SQL")
        self.assertEqual(result, "python sql")

    def test_empty_text(self):
        result = clean_resume_text("")
        self.assertEqual(result, "")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            clean_resume_text(123)


if __name__ == "__main__":
    unittest.main()
