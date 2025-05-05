import os
import pandas as pd

DATASET_NAME = "katehighnam/beth-dataset"
DATASET_DIR = "dataset"
CURRENT_DIR = os.getcwd()
DATASET_PATH = os.path.join(CURRENT_DIR, DATASET_DIR)

evil_input_raw = {
    'userId': [1001],
    'processName': ['(sd-pam)'],
    'eventName': ['prctl'],
    'argsNum': [5],
    'returnValue': [0],
    'args': ["[{'name': 'option', 'type': 'int', 'value': 'PR_SET_PDEATHSIG'}, {'name': 'arg2', 'type': 'unsigned long', 'value': 15}, {'name': 'arg3', 'type': 'unsigned long', 'value': 140730094619080}, {'name': 'arg4', 'type': 'unsigned long', 'value': 139950094474910}, {'name': 'arg5', 'type': 'unsigned long', 'value': 0}]"]
}

suspicious_input_raw = {
    'userId': [1000],
    'processName': ["sleep"],
    'eventName': ["close"],
    'argsNum': [1],
    'returnValue': [0],
    'args': ["[{'name': 'fd', 'type': 'int', 'value': 1}]"]
}

benign_input_raw = {
    'userId': [101],
    'processName': ["systemd-resolve"],
    'eventName': ["close"],
    'argsNum': [1],
    'returnValue': [0],
    'args': ["[{'name': 'fd', 'type': 'int', 'value': 15}]"]
}


EVIL_INPUT = pd.DataFrame(evil_input_raw)
SUSPICIOUS_INPUT = pd.DataFrame(suspicious_input_raw)
BENIGN_INPUT = pd.DataFrame(benign_input_raw)
