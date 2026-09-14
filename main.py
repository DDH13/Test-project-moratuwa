import pandas as pd

DATA_FILE = "Education_numerical.csv"

def load_data(path=DATA_FILE):
    return pd.read_csv(path)

def task_10_heavy_studiers(df):
    result = int((df["study_hours_week"] > 10).sum())
    print("Students who study more than 10 hours a week:", result)
    return result
def run_analysis(df):
    print("Dataset shape:", df.shape)
    print(df.head())
 
    task_10_heavy_studiers(df)
def main():
    df = load_data()
    run_analysis(df)
if __name__ == "__main__":
    main()
