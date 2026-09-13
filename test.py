"""
Automated checks for the Git Collaboration Assignment.

What this checks, for each of the 13 tasks:
  1. Your function exists under the required name in main.py.
  2. Calling it does not raise an exception.
  3. Its result matches an answer computed independently, straight from the
     CSV (for plot/export tasks, that the expected output file was created
     and contains the right numbers).

This also acts as an integration check: importing main.py runs every
STUDENT IMPORTS line and defines every STUDENT FUNCTIONS entry, so a bad
merge (duplicate def, broken indentation, leftover conflict markers) will
surface here before you even get to see a comparison against the reference
answer.

Usage:
    python test.py        # check every task
    python test.py 4       # check only task 4
"""
import importlib
import math
import os
import sys

import pandas as pd

DATA_FILE = "Education_numerical.csv"
RESULTS = []


def record(task_num, name, passed, detail=""):
    RESULTS.append((task_num, name, passed, detail))
    status = "PASS" if passed else "FAIL"
    suffix = f": {detail}" if detail and not passed else ""
    print(f"[{status}] Task {task_num:>2} - {name}{suffix}")


def close(a, b, tol=1e-2):
    try:
        return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)
    except (TypeError, ValueError):
        return a == b


def import_main():
    try:
        import main as student_main
        importlib.reload(student_main)
        return student_main
    except Exception as e:
        print(f"FATAL: main.py could not even be imported — {e!r}")
        print("This usually means a merge left behind a syntax error or")
        print("unresolved conflict markers ('<<<<<<<', '=======', '>>>>>>>').")
        sys.exit(1)


def check(mod, task_num, func_name, expect_fn=None, file_check=None, df=None):
    func = getattr(mod, func_name, None)
    if func is None:
        record(task_num, func_name, False, "function not found (not implemented yet)")
        return

    try:
        result = func(df.copy())
    except Exception as e:
        record(task_num, func_name, False, f"raised an exception: {e!r}")
        return

    if file_check:
        path, checker = file_check
        if not os.path.exists(path):
            record(task_num, func_name, False, f"expected output file '{path}' not found")
            return
        ok, detail = checker(path)
        record(task_num, func_name, ok, detail)
        return

    ok, detail = expect_fn(result)
    record(task_num, func_name, ok, detail)


def nonempty_file(path):
    return os.path.getsize(path) > 0, f"file '{path}' exists but is empty"


def run(only=None):
    df = pd.read_csv(DATA_FILE)
    mod = import_main()

    def want(n):
        return only is None or only == n

    if want(1):
        expected = (df.shape, df.columns.tolist())
        check(mod, 1, "task_01_dataset_overview", df=df,
              expect_fn=lambda r: (tuple(r) == expected, f"got {r!r}, expected {expected!r}"))

    if want(2):
        expected = (df.head(5)["student_id"].tolist(), df.tail(5)["student_id"].tolist())
        check(mod, 2, "task_02_preview_data", df=df,
              expect_fn=lambda r: (tuple(map(list, r)) == expected, f"got {r!r}, expected {expected!r}"))

    if want(3):
        expected = (df.isnull().sum().to_dict(), int(df.duplicated().sum()))
        check(mod, 3, "task_03_data_quality", df=df,
              expect_fn=lambda r: (tuple(r) == expected, f"got {r!r}, expected {expected!r}"))

    if want(4):
        expected = df.sort_values("predicted_score", ascending=False).head(10)["student_id"].tolist()
        check(mod, 4, "task_04_top_scorers", df=df,
              expect_fn=lambda r: (list(r) == expected, f"got {r!r}, expected {expected!r}"))

    if want(5):
        expected = df.sort_values("predicted_score", ascending=True).head(10)["student_id"].tolist()
        check(mod, 5, "task_05_bottom_scorers", df=df,
              expect_fn=lambda r: (list(r) == expected, f"got {r!r}, expected {expected!r}"))

    if want(6):
        expected = (df["study_hours_week"].mean(), df["study_hours_week"].max())
        check(mod, 6, "task_06_study_habits", df=df,
              expect_fn=lambda r: (close(r[0], expected[0]) and close(r[1], expected[1]),
                                    f"got {r!r}, expected {expected!r}"))

    if want(7):
        expected = {
            "small": int((df["class_size"] < 20).sum()),
            "medium": int(((df["class_size"] >= 20) & (df["class_size"] <= 40)).sum()),
            "large": int((df["class_size"] > 40).sum()),
        }
        check(mod, 7, "task_07_class_size_groups", df=df,
              expect_fn=lambda r: (dict(r) == expected, f"got {r!r}, expected {expected!r}"))

    if want(8):
        check(mod, 8, "task_08_score_distribution_plot", df=df,
              file_check=("overall_avg_hist.png", nonempty_file))

    if want(9):
        check(mod, 9, "task_09_study_vs_score_plot", df=df,
              file_check=("study_vs_predicted.png", nonempty_file))

    if want(10):
        expected = int((df["study_hours_week"] > 10).sum())
        check(mod, 10, "task_10_heavy_studiers", df=df,
              expect_fn=lambda r: (int(r) == expected, f"got {r!r}, expected {expected!r}"))

    if want(11):
        expected = (df["improvement_rate"] > 1).mean() * 100
        check(mod, 11, "task_11_improvement_check", df=df,
              expect_fn=lambda r: (close(r, expected), f"got {r!r}, expected ~{expected:.2f}"))

    if want(12):
        expected = df["peak_study_time"].value_counts().idxmax()
        check(mod, 12, "task_12_most_common_study_time", df=df,
              expect_fn=lambda r: (r == expected, f"got {r!r}, expected {expected!r}"))

    if want(13):
        def checker(path):
            out = pd.read_csv(path)
            expected_vals = {
                "min": df["predicted_score"].min(),
                "max": df["predicted_score"].max(),
                "mean": df["predicted_score"].mean(),
            }
            found, missing = set(), set()
            for stat, val in expected_vals.items():
                matched = False
                if stat in out.columns:
                    matched = close(out[stat].iloc[0], val)
                elif {"stat", "value"} <= set(out.columns):
                    row = out[out["stat"].astype(str).str.lower() == stat]
                    if not row.empty:
                        matched = close(row["value"].iloc[0], val)
                (found if matched else missing).add(stat)
            return not missing, f"missing/incorrect stats in CSV: {missing}" if missing else ""

        check(mod, 13, "task_13_summary_export", df=df,
              file_check=("summary_report.csv", checker))

    print()
    total, passed = len(RESULTS), sum(ok for _, _, ok, _ in RESULTS)
    print(f"{passed}/{total} tasks passing")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    only_task = int(sys.argv[1]) if len(sys.argv) > 1 else None
    run(only_task)
