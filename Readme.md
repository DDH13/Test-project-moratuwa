# Problem Description
The objective of this task is to ensure data integrity within the dataset by implementing a data quality check. Real-world datasets often contain missing, null, or corrupted values that can lead to incorrect analytical results or system failures. Therefore, a validation process is required to check for missing student records.
# Solution
Implemented the task_03_data_quality() function in main.py to inspect the student dataset for completeness:
* Iterates through the student records to check for missing essential fields (id, name, and class).
* Counts and returns the total number of incomplete records.
* Verified the implementation against the dataset, resulting in **0 missing records**.
