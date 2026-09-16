import pandas as pd

# === STUDENT IMPORTS: add your import below, one per line ===
# Example: import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

DATA_FILE = "Education_numerical.csv"


def load_data(path=DATA_FILE):
    return pd.read_csv(path)


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


def run_analysis(df):
    print("Dataset shape:", df.shape)
    print(df.head())

    # === STUDENT CALLS: register your function call below ===
    # Example: task_00_example(df)
    task_08_score_distribution_plot(df)

def main():
    df = load_data()
    run_analysis(df)


if __name__ == "__main__":
    main()
