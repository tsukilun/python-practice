from collections import Counter


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented - use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = []
        high_performers = 0

        for student in self.students:
            try:
                gpa = float(student["GPA"])
            except (KeyError, ValueError):
                print(
                    f"Warning: could not convert value for student "
                    f"{student.get('student_id', 'unknown')} - skipping row."
                )
                continue

            gpas.append(gpa)
            if gpa > 3.5:
                high_performers += 1

        if not gpas:
            self.result = {
                "analysis": "GPA Statistics",
                "total_students": len(self.students),
                "average_gpa": 0,
                "max_gpa": 0,
                "min_gpa": 0,
                "high_performers": 0,
            }
            return self.result

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
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        countries = [
            student["country"]
            for student in self.students
            if student.get("country")
        ]
        country_counts = Counter(countries)
        self.result = {
            "analysis": "Country Analysis",
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": country_counts.most_common(3),
            "all_countries": dict(country_counts),
        }
        return self.result

    def print_results(self):
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"
