import os

from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import CountryAnalyser, GpaAnalyser


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "students.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "result.json")


def main():
    fm = FileManager(DATA_FILE)
    if not fm.check_file():
        print("Stopping program.")
        return

    fm.create_output_folder(OUTPUT_DIR)

    dl = DataLoader(DATA_FILE)
    dl.load()
    dl.preview()

    analysers = [GpaAnalyser(dl.students), CountryAnalyser(dl.students)]

    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)
    for analyser in analysers:
        print(analyser)
        analyser.analyse()
        analyser.print_results()

    saver = ResultSaver(analysers[0].result, OUTPUT_FILE)
    report = Report(analysers[0], saver)
    report.generate()


if __name__ == "__main__":
    main()
