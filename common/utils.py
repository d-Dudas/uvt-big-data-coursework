from common.constants import get_dataset_path

import os
import sys

def is_processed_data(filename: str) -> bool:
    processed_data_keywords = ["testing", "training", "validation"]
    for keyword in processed_data_keywords:
        if keyword in filename.lower():
            return True
        
def is_csv_file(filename: str) -> bool:
    return filename.endswith(".csv") and not filename.startswith(".")

def is_dns_file(filename: str) -> bool:
    return "dns" in filename.lower()

def check_path(path: str):
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        sys.exit(1)

def is_cleaned_file(filename: str) -> bool:
    return "_cleaned" in filename.lower()

def get_dns_files(path = get_dataset_path()) -> list:
    check_path(path)

    dns_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if (is_csv_file(file) and
                not is_cleaned_file(file) and
                is_dns_file(file) and
                not is_processed_data(file)):
                dns_files.append(os.path.join(root, file))

    return dns_files

def get_cleaned_dns_files(path = get_dataset_path()) -> list:
    check_path(path)

    dns_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if (is_csv_file(file) and
                is_cleaned_file(file) and
                is_dns_file(file) and
                not is_processed_data(file)):
                dns_files.append(os.path.join(root, file))

    return dns_files

def get_syscall_files(path = get_dataset_path()) -> list:
    check_path(path)

    non_dns_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if (is_csv_file(file) and
                not is_cleaned_file(file) and
                not is_dns_file(file) and
                not is_processed_data(file)):
                non_dns_files.append(os.path.join(root, file))

    return non_dns_files

def get_cleaned_syscall_files(path = get_dataset_path()) -> list:
    check_path(path)

    non_dns_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if (is_csv_file(file) and 
                is_cleaned_file(file) and
                not is_dns_file(file) and
                not is_processed_data(file)):
                non_dns_files.append(os.path.join(root, file))

    return non_dns_files
