
import pandas as pd


def load_dataset(file_path):
    """
    Load a resume dataset from a CSV file.
    """

    try:
        dataset = pd.read_csv(file_path)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Dataset not found at: {file_path}"
        )

    if dataset.empty:
        raise ValueError("The dataset is empty.")

    return dataset


def validate_dataset(dataset):
    """
    Check whether the dataset contains the required columns.
    """

    required_columns = [
        "resume_text",
        "job_description",
        "label"
    ]

    for column in required_columns:

        if column not in dataset.columns:
            raise ValueError(
                f"Missing required column: {column}"
            )

    return True
