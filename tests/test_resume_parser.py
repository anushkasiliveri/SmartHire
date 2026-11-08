
import unittest
from io import BytesIO

from src.data_processing.resume_parser import extract_resume_text


class TestResumeParser(unittest.TestCase):

    def test_txt_resume_extraction(self):

        resume = BytesIO(
            b"Python, SQL, Machine Learning"
        )

        resume.name = "candidate.txt"

        result = extract_resume_text(resume)

        self.assertIn("Python", result)
        self.assertIn("SQL", result)

    def test_empty_resume(self):

        resume = BytesIO(b"")
        resume.name = "empty.txt"

        with self.assertRaises(ValueError):
            extract_resume_text(resume)

    def test_unsupported_file(self):

        resume = BytesIO(b"sample content")
        resume.name = "candidate.docx"

        with self.assertRaises(ValueError):
            extract_resume_text(resume)


if __name__ == "__main__":
    unittest.main()
