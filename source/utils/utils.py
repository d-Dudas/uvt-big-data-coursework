import os
import sys
import source.utils.constants as constants

def check_path(path: str):
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        sys.exit(1)

def is_csv_file(filename: str) -> bool:
    return filename.endswith(".csv") and not filename.startswith(".")

def is_cleaned_file(filename: str) -> bool:
    return "_cleaned" in filename.lower()

def get_datafiles() -> list:
    check_path(constants.DATASET_PATH)

    datafiles = []
    for root, _, files in os.walk(constants.DATASET_PATH):
        for file in files:
            if (is_csv_file(file) and
                not is_cleaned_file(file)):
                datafiles.append(os.path.join(root, file))

    return datafiles

def get_cleaned_datafiles() -> list:
    check_path(constants.DATASET_PATH)

    datafiles = []
    for root, _, files in os.walk(constants.DATASET_PATH):
        for file in files:
            if (is_csv_file(file) and 
                is_cleaned_file(file)):
                datafiles.append(os.path.join(root, file))

    return datafiles
