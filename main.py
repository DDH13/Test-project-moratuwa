import pandas as pd

# === STUDENT IMPORTS: add your import below, one per line ===
# Example: import matplotlib.pyplot as plt


DATA_FILE = "Education_numerical.csv"


def load_data(path=DATA_FILE):
    return pd.read_csv(path)


# === STUDENT FUNCTIONS: add your function below ===
# Each function must be named task_<NN>_<slug>(df) per the table in Readme.md,
# and must return its result (not just print it) so test.py can check it.
def task_01_dataset_overview(df):
    shape = df.shape
    columns_list = df.columns.tolist()

    print("Task 1 - Dataset overview")
    print("Number of rows:", shape[0])
    print("Number of columns:", shape[1])
    print("Column names:", columns_list)

    return shape, columns_list

def run_analysis(df):
    print("Dataset shape:", df.shape)
    print(df.head())

    # === STUDENT CALLS: register your function call below ===
    # Example: task_00_example(df)
    task_01_dataset_overview(df)

def main():
    df = load_data()
    run_analysis(df)


if __name__ == "__main__":
    main()
