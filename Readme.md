# Problem Description
The objective of this task is to ensure data integrity within the dataset by implementing a data quality check. Real-world datasets often contain missing, null, or corrupted values that can lead to incorrect analytical results or system failures. Therefore, a validation process is required to check for missing student records.
# Solution
Implemented `task_03_data_quality(df)` using Pandas to validate data quality across student records:
* Calculates missing values per column (`missing_counts_dict`).
* Identifies total duplicate rows (`duplicate_count`).
* Returns a tuple: `(missing_counts_dict, duplicate_count)`.
