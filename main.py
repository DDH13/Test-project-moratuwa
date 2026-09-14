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
def task_09_study_vs_score_plot(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x='study_hours_week', y='predicted_score', ax=ax)
    ax.set_title('Study Hours vs Predicted Score')
    ax.set_xlabel('Study Hours Per Week')
    ax.set_ylabel('Predicted Score')
    
    # Image file එක save කිරීම
    fig.savefig('study_vs_predicted.png')
    return fig
def run_analysis(df):
    print("Dataset shape:", df.shape)
    print(df.head())

    # === STUDENT CALLS: register your function call below ===
    # Example: task_00_example(df)
    task_09_study_vs_score_plot(df) 

def main():
    df = load_data()
    run_analysis(df)


if __name__ == "__main__":
    main()
