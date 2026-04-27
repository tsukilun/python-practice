import csv
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.abspath(os.path.join(BASE_DIR, "..", "students.csv"))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "result.json")


print("Checking file...")
if not os.path.exists(DATA_FILE):
    print("Error: students.csv not found. Please download the file from LMS.")
    exit()

print("File found: students.csv")
print("Checking output folder...")
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    print("Output folder created: output/")
else:
    print("Output folder already exists: output/")

students = []
with open(DATA_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

print(f"Total students: {len(students)}")
print("First 5 rows:")
print("-" * 30)
for student in students[:5]:
    print(
        f"{student['student_id']} | {student['age']} | {student['gender']} | "
        f"{student['country']} | GPA: {student['GPA']}"
    )
print("-" * 30)

gpas = []
high_performers = 0

for student in students:
    gpa = float(student["GPA"])
    gpas.append(gpa)
    if gpa > 3.5:
        high_performers += 1

avg_gpa = round(sum(gpas) / len(gpas), 2)
max_gpa = max(gpas)
min_gpa = min(gpas)

print("-" * 30)
print("GPA Analysis")
print("-" * 30)
print(f"Total students : {len(students)}")
print(f"Average GPA : {avg_gpa}")
print(f"Highest GPA : {max_gpa}")
print(f"Lowest GPA : {min_gpa}")
print(f"Students GPA>3.5 : {high_performers}")
print("-" * 30)

result = {
    "analysis": "GPA Statistics",
    "total_students": len(students),
    "average_gpa": avg_gpa,
    "max_gpa": max_gpa,
    "min_gpa": min_gpa,
    "high_performers": high_performers,
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4)

print("=" * 30)
print("ANALYSIS RESULT")
print("=" * 30)
print("Analysis : GPA Statistics")
print(f"Total students : {result['total_students']}")
print(f"Average GPA : {result['average_gpa']}")
print(f"Highest GPA : {result['max_gpa']}")
print(f"Lowest GPA : {result['min_gpa']}")
print(f"High performers : {result['high_performers']}")
print("=" * 30)
print("Result saved to output/result.json")
