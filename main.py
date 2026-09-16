import pandas as pd

# === STUDENT IMPORTS: add your import below, one per line ===
import matplotlib.pyplot as plt

DATA_FILE = "Education_numerical.csv"


def load_data(path=DATA_FILE):
    return pd.read_csv(path)


# === STUDENT FUNCTIONS: add your function below ===

def task_05_bottom_scorers(df):
    bottom = df.sort_values("predicted_score", ascending=True).head(10)
    result = bottom["student_id"].tolist()
    print("Bottom 10 scorers:", result)
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
def task_12_most_common_study_time(df):
    return df["peak_study_time"].value_counts().idxmax()

def run_analysis(df):
    print("Dataset shape:", df.shape)
    print(df.head())

    # === STUDENT CALLS: register your function call below ===
    task_05_bottom_scorers(df)
    task_12_most_common_study_time(df)
    task_08_score_distribution_plot(df)

def main():
    df = load_data()
    run_analysis(df)


if __name__ == "__main__":
    main()