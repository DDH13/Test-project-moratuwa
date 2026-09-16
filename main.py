import random


# === STUDENT IMPORTS: add your import below, one per line ===

# Example: import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

DATA_FILE = "Education_numerical.csv"


def load_data(path=DATA_FILE):
    return pd.read_csv(path)
def task_08_score_distribution_plot(df):
    plt.figure()
    df["overall_avg"].plot(kind="hist", bins=10, edgecolor="black")
    plt.xlabel("Overall Average")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Overall Average Scores")
    output_path = "overall_avg_hist.png"
    plt.savefig(output_path)
    plt.close()
    return output_path

def task_12_most_common_study_time(df):
    return df["peak_study_time"].value_counts().idxmax()


# Task 03: Data Quality Check Function (Updated for DataFrame)
def task_03_data_quality(df):
    missing_counts_dict = df.isnull().sum().to_dict()
    duplicate_count = int(df.duplicated().sum())
    return (missing_counts_dict, duplicate_count)
# === STUDENT FUNCTIONS: add your function below ===
def task_08_score_distribution_plot(df):
    plt.figure()
    df["overall_avg"].plot(kind="hist", bins=10, edgecolor="black")
    plt.xlabel("Overall Average")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Overall Average Scores")
    output_path = "overall_avg_hist.png"
    plt.savefig(output_path)
    plt.close()
    return output_path
# Each function must be named task_<NN>_<slug>(df) per the table in Readme.md,
# and must return its result (not just print it) so test.py can check it.
#
# Example
#
# def task_00_example(df):
#     result = int((df["quiz_attempts"] > 5).sum())
#     print("Students with more than 5 quiz attempts:", result)
#     return result

def task_12_most_common_study_time(df):
    return df["peak_study_time"].value_counts().idxmax()

df= load_data()
missing_dict, duplicates = task_03_data_quality(df)

task_12_most_common_study_time(df)
task_08_score_distribution_plot(df)

print(f"Missing values per column: {missing_dict}")
print(f"Duplicate rows count: {duplicates}")

   

