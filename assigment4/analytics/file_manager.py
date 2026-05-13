import os


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

    def create_output_folder(self, folder):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print("Output folder created: output/")
        else:
            print("Output folder already exists: output/")
