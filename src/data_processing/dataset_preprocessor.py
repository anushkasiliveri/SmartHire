
import pandas as pd

from src.data_processing.text_cleaner import clean_resume_text


def preprocess_dataset(dataset):
    """
    Clean and prepare resume dataset for machine learning.
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

    # Create a copy to avoid modifying the original dataset
    dataset = dataset.copy()

    # Remove rows with missing values
    dataset = dataset.dropna(
        subset=required_columns
    )

    # Clean resume text
    dataset["resume_text"] = dataset[
        "resume_text"
    ].apply(clean_resume_text)

    # Clean job description
    dataset["job_description"] = dataset[
        "job_description"
    ].apply(clean_resume_text)

    # Remove rows containing empty text
    dataset = dataset[
        (dataset["resume_text"] != "") &
        (dataset["job_description"] != "")
    ]

    # Reset row numbering
    dataset = dataset.reset_index(drop=True)

    return dataset
