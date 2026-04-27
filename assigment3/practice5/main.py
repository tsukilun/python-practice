import csv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.abspath(os.path.join(BASE_DIR, "..", "students.csv"))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


def check_files():
    print("Checking file...")
    if not os.path.exists(DATA_FILE):
        print("Error: students.csv not found. Please download the file from LMS.")
        return False

    print("File found: students.csv")
    print("Checking output folder...")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")

    return True


def load_data(filename):
    print("Loading data...")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students = list(reader)
        print(f"Data loaded successfully: {len(students)} students")
        return students
    except FileNotFoundError:
        display_name = os.path.basename(filename)
        print(f"Error: File '{display_name}' not found. Please check the filename.")
        return []
    except Exception as error:
        print(f"Error while loading data: {error}")
        return []


def preview_data(students, n=5):
    print(f"First {n} rows:")
    print("-" * 30)
    for student in students[:n]:
        print(
            f"{student['student_id']} | {student['age']} | {student['gender']} | "
            f"{student['country']} | GPA: {student['GPA']}"
        )
    print("-" * 30)


def analyse_gpa(students):
    gpas = []
    high_performers = 0

    for student in students:
        try:
            gpa = float(student["GPA"])
        except ValueError:
            print(
                f"Warning: could not convert value for student "
                f"{student.get('student_id', 'unknown')} - skipping row."
            )
            continue

        gpas.append(gpa)
        if gpa > 3.5:
            high_performers += 1

    result = {
        "analysis": "GPA Statistics",
        "total_students": len(students),
        "average_gpa": round(sum(gpas) / len(gpas), 2),
        "max_gpa": max(gpas),
        "min_gpa": min(gpas),
        "high_performers": high_performers,
    }

    print("-" * 30)
    print("GPA Analysis")
    print("-" * 30)
    print(f"Total students : {result['total_students']}")
    print(f"Average GPA : {result['average_gpa']}")
    print(f"Highest GPA : {result['max_gpa']}")
    print(f"Lowest GPA : {result['min_gpa']}")
    print(f"Students GPA>3.5 : {result['high_performers']}")
    print("-" * 30)

    return result


def lambda_map_filter(students):
    high_gpa = list(filter(lambda s: float(s["GPA"]) > 3.8, students))
    gpa_values = list(map(lambda s: float(s["GPA"]), students))
    hard_workers = list(
        filter(lambda s: float(s["study_hours_per_day"]) > 4, students)
    )

    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)
    print(f"Students with GPA > 3.8 : {len(high_gpa)}")
    print(f"GPA values (first 5) : {gpa_values[:5]}")
    print(f"Students studying > 4 hrs : {len(hard_workers)}")
    print("-" * 30)


def main():
    if not check_files():
        return

    students = load_data(DATA_FILE)
    if not students:
        return

    preview_data(students)
    analyse_gpa(students)
    lambda_map_filter(students)

    load_data(DATA_FILE)
    wrong_file = os.path.join(BASE_DIR, "wrong_file.csv")
    load_data(wrong_file)


if __name__ == "__main__":
    main()
