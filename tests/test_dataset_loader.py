
import unittest
import pandas as pd
import tempfile
import os

from src.data_processing.dataset_loader import (
    load_dataset,
    validate_dataset
)


class TestDatasetLoader(unittest.TestCase):

    def test_load_dataset(self):

        data = {
            "resume_text": ["Python developer"],
            "job_description": ["Python skills required"],
            "label": [1]
        }

        with tempfile.TemporaryDirectory() as folder:

            file_path = os.path.join(folder, "test.csv")

            pd.DataFrame(data).to_csv(
                file_path, index=False
            )

            result = load_dataset(file_path)

            self.assertEqual(len(result), 1)

    def test_validate_dataset(self):

        data = pd.DataFrame({
            "resume_text": ["Python developer"],
            "job_description": ["Python skills required"],
            "label": [1]
        })

        self.assertTrue(validate_dataset(data))

    def test_missing_column(self):

        data = pd.DataFrame({
            "resume_text": ["Python developer"],
            "label": [1]
        })

        with self.assertRaises(ValueError):
            validate_dataset(data)

    def test_missing_file(self):

        with self.assertRaises(FileNotFoundError):
            load_dataset("missing_dataset.csv")


if __name__ == "__main__":
    unittest.main()
