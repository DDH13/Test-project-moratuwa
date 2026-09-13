import pandas as pd

# === STUDENT IMPORTS: add your import below, one per line ===


DATA_FILE = "Education_numerical.csv"


def load_data(path=DATA_FILE):
    return pd.read_csv(path)


# === STUDENT FUNCTIONS: add your function below ===

def task_05_bottom_scorers(df):
    bottom = df.sort_values("predicted_score", ascending=True).head(10)
    result = bottom["student_id"].tolist()
    print("Bottom 10 scorers:", result)
    return result


def run_analysis(df):
    print("Dataset shape:", df.shape)
    print(df.head())

    # === STUDENT CALLS: register your function call below ===
    task_05_bottom_scorers(df)


def main():
    df = load_data()
    run_analysis(df)


if __name__ == "__main__":
    main()