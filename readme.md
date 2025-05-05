# Big Data Coursework

## Dependencies

- python 3.8 or higher
- pipenv

## Setup

### 1. Install pip packages

```
pipenv install
```

### 2. Bootstrap

The bootstrap.py script will automatically download the data and remove  
unnecessary files.

```
cd source
./bootstrap.py
```

### 3. Process data

The process_data.py script will create some cleaned datafiles.

**We will only keep the bolded features:**  

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

```
./process_data.py
```

### 4. Setup ready for Jupyter Notebook Files.

## Dataset

[BETH dataset](https://www.kaggle.com/datasets/katehighnam/beth-dataset)

## Requierements

### Main goal

Solve a real-life problem using a dataset and demonstrate Big Data principles,  
following the CRISP-DM lifecycle.

### CRISP-DM Lifecycle Overview

1. **Business Understanding**: What real-world problem are you trying to solve?
2. **Data Understanding**: Explore BETH dataset: What's in it? What could it  
   help solve?
3. **Data Preparation**: Clean and prepare the data for analysis (handle  
   missing values, standardize formats, etc).
4. **Modeling**: Use machine learning or analytics to find patterns or make  
   predictions.
5. **Evaluation**: Test your results and check if they solve the problem.
6. **Deployment**: A report or presentation to share your findings and  
   solutions.

### Deliverables

- 60% of the grade -> 5-minute presentation
  - present the problem, it's relevance, the dataset, any legal/ethical
    concerns (LSEPI = Legal, Social, Ethical, Privacy, and Intellectual
    property), and your CRISP-DM process.
- 40% of the grade -> 5-minute code demo
  - show the code, run it live, explain a technical challange you overcome
