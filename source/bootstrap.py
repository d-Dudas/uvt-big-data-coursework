#!/usr/bin/env python3

import kagglehub
import source.utils.constants as constants
import os
import shutil

def remove_unused_files():
    removed_files = 0
    for root, _, files in os.walk(constants.DATASET_PATH):
        for file in files:
            if "-ip-" not in file.lower() or "dns" in file.lower():
                os.remove(os.path.join(root, file))
                removed_files += 1

    print(f"Removed {removed_files} DNS files from the dataset.")

def download_dataset():
    if os.path.exists(constants.DATASET_PATH):
        print("Dataset already exists at:", constants.DATASET_PATH)
        return

    default_download_path = kagglehub.dataset_download(constants.DATASET_NAME)

    if os.path.exists(default_download_path):
        print("Dataset downloaded successfully. Path:", default_download_path)
        print("Moving dataset to current working directory...")
        shutil.move(default_download_path, constants.DATASET_PATH)
        print("Dataset moved to:", constants.DATASET_PATH)
        print("Removing DNS files...")
        remove_unused_files()
    else:
        print("Failed to download the dataset.")


if __name__ == "__main__":
    download_dataset()
