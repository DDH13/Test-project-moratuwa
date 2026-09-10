import random

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

print(f"Students: {len(students)}")
print(f"Teachers: {len(teachers)}")
print(f"Classes: {len(classes)}")
print(f"Subjects: {len(subjects)}")
