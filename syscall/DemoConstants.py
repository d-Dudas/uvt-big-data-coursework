import pandas as pd

# Example input sample
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


evil_input = pd.DataFrame(evil_input_raw)
suspicious_input = pd.DataFrame(suspicious_input_raw)
benign_input = pd.DataFrame(benign_input_raw)
