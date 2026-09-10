# Problem Description

## Git Collaboration Assignment — Merging Without Breaking `main`

### Learning objectives

By the end of this assignment you will have practiced:

- Creating a feature branch and keeping your changes isolated to it
- Opening a pull request (PR) on GitHub
- Reviewing a classmate's PR
- Pulling in upstream changes and **resolving a real merge conflict** without deleting anyone else's work
- Verifying that a shared codebase still runs after every merge

### The scenario

This repo contains `main.py`, a small script that loads `Education_numerical.csv` (a dataset of student performance metrics) into a pandas DataFrame and runs some analysis. Each of the **13 students** in this class is assigned exactly one analysis feature to add. Every feature must be wired into the same three marked sections of `main.py`:

```python
# === STUDENT IMPORTS: ... ===
# === STUDENT FUNCTIONS: ... ===
# === STUDENT CALLS: ... ===
```

### Setup

1. Fork and clone the repo and check that the baseline runs before you touch anything:
   ```
   pip install -r requirements.txt
   python main.py
   ```
2. Create your branch: `feature/<lastname>-<short-task-name>` (e.g. `feature/silva-top-scorers`).

### Workflow rules

1. Only add code — never delete or rewrite a classmate's function, import, or call, even if it's already conflicting with yours in a merge. Add your lines alongside theirs.
2. Commit your change and push your branch, then open a PR into `main`.
3. PRs merge in **sign-up order** (published by the instructor) — first come, first merged. If you're not first, `main` will already contain other students' code by the time you PR.
4. Before your PR can merge:
   - `git pull origin main` (or merge `main` into your branch) to bring in everyone merged before you.
   - Resolve any conflicts locally — keep both sides' additions inside each `STUDENT` block.
   - Run `python main.py` and confirm it still completes with no errors.
   - Run `python test.py` and confirm every previously-passing task (not just yours) still passes.
   - Push the resolved branch.
5. Get at least one classmate's review/approval on your PR before merging.

### The 13 tasks

Each task takes the DataFrame `df` (loaded from `Education_numerical.csv`) and both prints/plots your result **and returns it**, so `test.py` (see below) can check your work automatically. Implement yours as a single function, named exactly as shown below, in the `STUDENT FUNCTIONS` block, and call it from the `STUDENT CALLS` block inside `run_analysis`.

No statistics background is assumed — every task only needs basic pandas methods (`.shape`, `.head()`, `.sort_values()`, `.mean()`, `.max()`, `.value_counts()`, simple filtering with `[ ]`) or a one-line plot.

| # | Task | Required function name | What to do | Return value | Import needed |
|---|------|------------------------|------------|---------------|----------------|
| 1 | Dataset overview | `task_01_dataset_overview(df)` | Get `df.shape` and `df.columns.tolist()` | `(shape, columns_list)` | *(none extra)* |
| 2 | Preview the data | `task_02_preview_data(df)` | Get the first 5 rows and last 5 rows (`df.head()`, `df.tail()`) | `(head_ids, tail_ids)` — each a list of `student_id` | *(none extra)* |
| 3 | Data quality check | `task_03_data_quality(df)` | Count missing values per column and duplicate rows | `(missing_counts_dict, duplicate_count)` | *(none extra)* |
| 4 | Top scorers | `task_04_top_scorers(df)` | Sort by `predicted_score` (highest first), take the top 10 | list of 10 `student_id` | *(none extra)* |
| 5 | Students who need help | `task_05_bottom_scorers(df)` | Sort by `predicted_score` (lowest first), take the bottom 10 | list of 10 `student_id` | *(none extra)* |
| 6 | Study habits | `task_06_study_habits(df)` | Average and maximum `study_hours_week` | `(average, maximum)` | *(none extra)* |
| 7 | Class size groups | `task_07_class_size_groups(df)` | Count students with `class_size` < 20 (small), 20–40 (medium), > 40 (large) | `{"small": n, "medium": n, "large": n}` | *(none extra)* |
| 8 | Score distribution plot | `task_08_score_distribution_plot(df)` | Plot a histogram of `overall_avg`, save to `overall_avg_hist.png` | the file path string | `matplotlib.pyplot` |
| 9 | Study vs. score plot | `task_09_study_vs_score_plot(df)` | Scatter plot `study_hours_week` vs. `predicted_score`, save to `study_vs_predicted.png` | the file path string | `matplotlib.pyplot` |
| 10 | Heavy studiers | `task_10_heavy_studiers(df)` | Count students who study more than 10 hours a week | integer count | *(none extra)* |
| 11 | Improvement check | `task_11_improvement_check(df)` | Percentage of students with `improvement_rate` greater than 1 | percentage (0–100) | *(none extra)* |
| 12 | Most common study time | `task_12_most_common_study_time(df)` | Most frequent value in `peak_study_time` (`.value_counts()`) | the value | *(none extra)* |
| 13 | Quick summary export | `task_13_summary_export(df)` | Write min, max, and average of `predicted_score` to `summary_report.csv` | the file path string | *(none extra)* |

Tasks 8 and 9 both need `matplotlib.pyplot` — expect an import-line conflict there, not just a function-block conflict. If a package you need isn't already in `requirements.txt`, add it there as part of your PR.

### Checking your work with `test.py`

`test.py` computes the correct answer for each task straight from the CSV, independently of your code, then calls your function and compares. It's the same check a reviewer or the instructor will run, so use it before you ever open a PR:

```
python test.py         # checks every task that's implemented so far
python test.py 4        # checks only task 4
```

Run it in two places in your workflow:
1. **Before opening your PR** — confirms your own function is correct.
2. **After resolving a merge conflict, before merging** — confirms the merge didn't break anyone else's already-passing task. Importing `main.py` during this check will also fail loudly if a conflict left behind leftover `<<<<<<<`/`=======`/`>>>>>>>` markers or broke another function's indentation.

### Grading rubric

| Criterion | Weight |
|---|---|
| `python test.py <your task number>` passes | 40% |
| Proper branch/PR workflow followed (branch name, PR opened, review requested) | 20% |
| Evidence of resolving a real merge conflict without deleting a classmate's code | 30% |
| `python test.py` (full run) still passes for everyone after your merge | 10% |

# Solution

To be filled in collaboratively as each student's PR is merged into `main`. Once all 13 PRs have landed, `main.py` should run all 13 analyses in sequence with no errors.
