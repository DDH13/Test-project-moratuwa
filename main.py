import pandas as pd

# === STUDENT IMPORTS: add your import below, one per line ===
# Example: import matplotlib.pyplot as plt


DATA_FILE = "Education_numerical.csv"


def load_data(path=DATA_FILE):
    return pd.read_csv(path)


# === STUDENT FUNCTIONS: add your function below ===
# Each function must be named task_<NN>_<slug>(df) per the table in Readme.md,
# and must return its result (not just print it) so test.py can check it.
#
# Example 
#
# def task_00_example(df):
#     result = int((df["quiz_attempts"] > 5).sum())
#     print("Students with more than 5 quiz attempts:", result)
#     return result

def task_06_study_habits(df):
    average = df["study_hours_week"].mean()
    maximum = df["study_hours_week"].max()
    
    result = (average, maximum)
    print("Study hours per week - Average:", average)
    print("Study hours per week - Maximum:", maximum)
    
    return result


def run_analysis(df):
    print("Dataset shape:", df.shape)
    print(df.head())

    # === STUDENT CALLS: register your function call below ===
    # Example: task_00_example(df)

    task_06_study_habits(df)


def main():
    df = load_data()
    run_analysis(df)


if __name__ == "__main__":
    main()
