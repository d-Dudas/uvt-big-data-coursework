#!/usr/bin/env python3

import pandas as pd
import source.utils.utils as utils

def assign_label(row):
    if row['evil'] == 1:
        return 'evil'
    elif row['sus'] == 1:
        return 'suspicious'
    else:
        return 'benign'
    
'''
### **The dataset have the following features:**  

- timestamp - not really useful for our ML model, since the timestamp is not relevant in the context of evilness of a call
- processId - not useful, since an evil process can have any ID
- parentProcessId - not useful, since an evil process' parent can have any ID
- **userId**
- **processName**
- hostName - not useful, since an attack can happen to any host
- eventId - not useful, since an evil event can have any ID
- **eventName**
- **argsNum**
- **returnValue**
- **args**
- **sus**
- **evil**
'''
COLUMNS_TO_KEEP = [
    'userId',
    'processName',
    'eventName',
    'argsNum',
    'returnValue',
    'args',
    'label'
]

def process_each_datafile(files):
    for file in files:
        print(f"Processing file: {file}")

        df = pd.read_csv(file)
        df['label'] = df.apply(assign_label, axis=1)
        df = df[COLUMNS_TO_KEEP]

        cleaned_file_name = file.split('.csv')[0] + '_cleaned.csv'
        df.to_csv(cleaned_file_name, index=False)
        print(f"Saving cleaned file: {cleaned_file_name}")

def main():
    datafiles = utils.get_datafiles()
    if not datafiles:
        print("No data files found.")
    else:
        print(f"Found {len(datafiles)} data files.")
        process_each_datafile(datafiles)

if __name__ == "__main__":
    main()
