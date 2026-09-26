import random


# === STUDENT IMPORTS: add your import below, one per line ===

# Example: import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt


import seaborn as sns

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
def task_04_top_scorers(df):
    top10 = df.sort_values("predicted_score", ascending=False).head(10)
    result = top10["student_id"].tolist()
    print("Top 10 scorers:", result)
    return result
# Each function must be named task_<NN>_<slug>(df) per the table in Readme.md,
# and must return its result (not just print it) so test.py can check it.
#
# Example
#
# def task_00_example(df):
#     result = int((df["quiz_attempts"] > 5).sum())
#     print("Students with more than 5 quiz attempts:", result)
#     return result

def task_01_dataset_overview(df):
    shape = df.shape
    columns_list = df.columns.tolist()

    print("Task 1 - Dataset overview")
    print("Number of rows:", shape[0])
    print("Number of columns:", shape[1])
    print("Column names:", columns_list)

    return shape, columns_list


def task_05_bottom_scorers(df):
    bottom = df.sort_values("predicted_score", ascending=True).head(10)
    result = bottom["student_id"].tolist()
    print("Bottom 10 scorers:", result)
    return result


def task_06_study_habits(df):
    average = df["study_hours_week"].mean()
    maximum = df["study_hours_week"].max()

    result = (average, maximum)
    print("Study hours per week - Average:", average)
    print("Study hours per week - Maximum:", maximum)

    return result


def task_07_class_size_groups(df):
    small = (df["class_size"] < 20).sum()
    medium = ((df["class_size"] >= 20) & (df["class_size"] <= 40)).sum()
    large = (df["class_size"] > 40).sum()
    result = {"small": int(small), "medium": int(medium), "large": int(large)}
    print(result)
    return result


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


def task_09_study_vs_score_plot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='study_hours_week', y='predicted_score', ax=ax)
    ax.set_title('Study Hours vs Predicted Score')
    ax.set_xlabel('Study Hours Per Week')
    ax.set_ylabel('Predicted Score')
    
    # Image file එක save කිරීම
    fig.savefig('study_vs_predicted.png')
    return fig


def task_11_improvement_check(df):
    percentage = (df["improvement_rate"] > 1).mean() * 100
    print("Percentage of students with improvement rate greater than 1:", percentage)
    return percentage


def task_12_most_common_study_time(df):
    return df["peak_study_time"].value_counts().idxmax()

df = load_data()
missing_dict, duplicates = task_03_data_quality(df)

    # === STUDENT CALLS: register your function call below ===

    task_04_top_scorers(df)
    # Example: task_00_example(df)

    task_01_dataset_overview(df)
    task_05_bottom_scorers(df)
    task_06_study_habits(df)
    task_07_class_size_groups(df)
    task_08_score_distribution_plot(df)
    task_09_study_vs_score_plot(df)
    task_11_improvement_check(df)
    task_12_most_common_study_time(df)


print(f"Missing values per column: {missing_dict}")
print(f"Duplicate rows count: {duplicates}")


