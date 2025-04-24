import os

DATASET_DIRECTORY = "dataset"

def get_dataset_path() -> str:
    return os.path.join(os.path.dirname(__file__), "..", DATASET_DIRECTORY)
