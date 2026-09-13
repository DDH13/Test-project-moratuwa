import random


# === STUDENT IMPORTS: add your import below, one per line ===

# Example: import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = "Education_numerical.csv"


def load_data(path=DATA_FILE):
    return pd.read_csv(path)



# Task 03: Data Quality Check Function (Updated for DataFrame)
def task_03_data_quality(df):
    missing_counts_dict = df.isnull().sum().to_dict()
    duplicate_count = int(df.duplicated().sum())
    return (missing_counts_dict, duplicate_count)


df= load_data()
missing_dict, duplicates = task_03_data_quality(df)

print(f"Missing values per column: {missing_dict}")
print(f"Duplicate rows count: {duplicates}")


