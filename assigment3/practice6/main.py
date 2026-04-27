import csv
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.abspath(os.path.join(BASE_DIR, "..", "students.csv"))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "result.json")


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print("File found: students.csv")
            return True

        print("Error: students.csv not found. Please download the file from LMS.")
        return False

    def create_output_folder(self, folder=OUTPUT_DIR):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Output folder created: output/")
        else:
            print("Output folder already exists: output/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print("Error: students.csv not found. Please download the file from LMS.")

        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for student in self.students[:n]:
            print(
                f"{student['student_id']} | {student['age']} | "
                f"{student['gender']} | {student['country']} | GPA: {student['GPA']}"
            )
        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high_performers = 0

        for student in self.students:
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

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high_performers,
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print(f"Total students : {self.result['total_students']}")
        print(f"Average GPA : {self.result['average_gpa']}")
        print(f"Highest GPA : {self.result['max_gpa']}")
        print(f"Lowest GPA : {self.result['min_gpa']}")
        print(f"Students GPA>3.5 : {self.result['high_performers']}")
        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as file:
                json.dump(self.result, file, indent=4)
            print("Result saved to output/result.json")
        except Exception as error:
            print(f"Error while saving result: {error}")


def main():
    fm = FileManager(DATA_FILE)
    if not fm.check_file():
        print("Stopping program.")
        exit()

    fm.create_output_folder()

    dl = DataLoader(DATA_FILE)
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, OUTPUT_FILE)
    saver.save_json()


if __name__ == "__main__":
    main()
