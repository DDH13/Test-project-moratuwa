import random
import pandas as pd

first_names = [
    "James", "Mary", "Robert", "Patricia", "Michael", "Jennifer", "William", "Linda",
    "David", "Barbara", "Richard", "Elizabeth", "Joseph", "Susan", "Thomas", "Jessica",
    "Charles", "Sarah", "Christopher", "Karen", "Daniel", "Nancy", "Matthew", "Lisa",
    "Mark", "Betty", "Donald", "Margaret", "Steven", "Sandra", "Paul", "Ashley",
    "Andrew", "Kimberly", "Joshua", "Emily", "Kenneth", "Donna", "Kevin", "Carol"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker"
]

def generate_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

students = [
    {"id": f"S{i:03d}", "name": generate_name(), "class": f"Class {(i % 5) + 1}"}
    for i in range(1, 31)
]

teachers = [
    {"id": f"T{i:03d}", "name": generate_name(), "subject": f"Subject {(i % 5) + 1}"}
    for i in range(1, 31)
]

classes = [
    {"id": f"C{i}", "name": f"Class {i}", "capacity": 30}
    for i in range(1, 6)
]

subjects = [
    {"id": f"Sub{i}", "name": f"Subject {i}"}
    for i in range(1, 6)
]
# Task 03: Data Quality Check Function (Updated for DataFrame)
def task_03_data_quality(df):
    missing_counts_dict = df.isnull().sum().to_dict()
    duplicate_count = int(df.duplicated().sum())
    return (missing_counts_dict, duplicate_count)

df_students = pd.DataFrame(students)

missing_dict, duplicates = task_03_data_quality(df_students)

print(f"Missing values per column: {missing_dict}")
print(f"Duplicate rows count: {duplicates}")

print(f"Students: {len(students)}")
print(f"Teachers: {len(teachers)}")
print(f"Classes: {len(classes)}")
print(f"Subjects: {len(subjects)}")

