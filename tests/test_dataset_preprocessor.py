
import unittest
import pandas as pd

from src.data_processing.dataset_preprocessor import preprocess_dataset


class TestDatasetPreprocessor(unittest.TestCase):

    def test_text_cleaning(self):

        data = pd.DataFrame({
            "resume_text": ["PYTHON DEVELOPER"],
            "job_description": ["PYTHON DEVELOPER REQUIRED"],
            "label": [1]
        })

        result = preprocess_dataset(data)

        self.assertEqual(
            result.loc[0, "resume_text"],
            "python developer"
        )

    def test_missing_values(self):

        data = pd.DataFrame({
            "resume_text": ["Python developer", None],
            "job_description": ["Python required", "Java required"],
            "label": [1, 0]
        })

        result = preprocess_dataset(data)

        self.assertEqual(len(result), 1)

    def test_empty_text_removal(self):

        data = pd.DataFrame({
            "resume_text": ["", "Python developer"],
            "job_description": ["Python required", "Python required"],
            "label": [0, 1]
        })

        result = preprocess_dataset(data)

        self.assertEqual(len(result), 1)

    def test_missing_column(self):

        data = pd.DataFrame({
            "resume_text": ["Python developer"],
            "label": [1]
        })

        with self.assertRaises(ValueError):
            preprocess_dataset(data)


if __name__ == "__main__":
    unittest.main()
