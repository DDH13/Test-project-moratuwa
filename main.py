import pandas as pd

# === STUDENT IMPORTS: add your import below, one per line ===
# Example: import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

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

def task_01_dataset_overview(df):
    shape = df.shape
    columns_list = df.columns.tolist()

    print("Task 1 - Dataset overview")
    print("Number of rows:", shape[0])
    print("Number of columns:", shape[1])
    print("Column names:", columns_list)

    return shape, columns_list

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
# Each function must be named task_<NN>_<slug>(df) per the table in Readme.md,
# and must return its result (not just print it) so test.py can check it.
#
# Example
#
# def task_00_example(df):
#     result = int((df["quiz_attempts"] > 5).sum())
#     print("Students with more than 5 quiz attempts:", result)
#     return result
def task_09_study_vs_score_plot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='study_hours_week', y='predicted_score', ax=ax)
    ax.set_title('Study Hours vs Predicted Score')
    ax.set_xlabel('Study Hours Per Week')
    ax.set_ylabel('Predicted Score')
    
    # Image file එක save කිරීම
    fig.savefig('study_vs_predicted.png')
    return fig

def task_12_most_common_study_time(df):
    return df["peak_study_time"].value_counts().idxmax()

def run_analysis(df):
    print("Dataset shape:", df.shape)
    print(df.head())

    # === STUDENT CALLS: register your function call below ===
    # Example: task_00_example(df)
    task_09_study_vs_score_plot(df) 
    task_01_dataset_overview(df)
    task_07_class_size_groups(df)
    task_08_score_distribution_plot(df)
    task_12_most_common_study_time(df)

def main():
    df = load_data()
    run_analysis(df)


if __name__ == "__main__":
    main()
