# command-line argument (1):
# URL to problem

# {1} = day_number

# {2} = problem_title

#################################################

# make new directory: "Day {1}"

# copy template Python file: "{2}.py"

# copy template Markdown file: "Outline.py"

# input formatted problem description into "Outline.py"

# create empty "sample.in" file

# download "input.in" file via URL

# copy template Python test file: "test_{2}.py"


from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup
import re
from os import getcwd, mkdir, path


class DayCreator:
    TEMPLATE_PATH: str = "./templates"

    def __init__(self, current_directory: str):
        self.current_dir: str = current_directory
        self.process_arguments()

    def create_new_day(self):
        self.get_url_data()
        self.check_year_directory()
        self.create_day_directory()
        self.create_files()

    def process_arguments(self):
        parser = ArgumentParser(
            prog="create_day.py",
            usage="python create_day.py <AdventOfCode.com URL>"
        )
        parser.add_argument("url")
        args = parser.parse_args()
        self.url: str = str(args.url).lower()
        if "adventofcode.com" not in self.url:
            parser.error(f"{self.url}: Please provide \"adventofcode.com\" URL.")

    def get_url_data(self):
        response = requests.get(self.url)
        self.html_content = BeautifulSoup(response.content, "html.parser")
        self.year: str = self.get_year()
        self.day_number, self.problem_title = self.get_problem_header()

    def get_year(self):
        header = self.html_content.find("h1", attrs={"class": "title-event"})
        year = re.search(r".*(\d{4}).*", header.text)
        return year.group(1)

    def get_problem_header(self) -> tuple[str]:
        problem_header: str =  self.html_content.find("h2").text.strip()
        day_match = re.search(r"\d", problem_header)
        title_match = re.search(r": (.+) -", problem_header)
        title: str = self.convert_to_filename(title_match.group(1))
        return (day_match.group(), title)

    def convert_to_filename(self, text: str) -> str:
        return text.lower().replace(" ", "_")

    def check_year_directory(self):
        self.year_dir: str = f"{self.current_dir}/{self.year}"
        if not path.isdir(self.current_dir):
            mkdir(self.year_dir)

    def create_day_directory(self):
        dir_name: str = f"Day {self.day_number}"
        try:
            mkdir(f"{self.year_dir}/{dir_name}")
        except:
            print(
                f"ERROR: directory \"{self.year_dir}/{dir_name}\" already exists."
            )
            exit()

    def create_files(self):
        self.create_python_file()
        self.create_markdown_file()
        self.create_sample_data_file()
        self.create_input_data_file()
        self.create_python_test_file()

    def create_python_file(self):
        pass
    
    def create_markdown_file(self):
        pass
    
    def create_sample_data_file(self):
        pass
    
    def create_input_data_file(self):
        pass
    
    def create_python_test_file(self):
        pass


if __name__ == "__main__":
    script = DayCreator(getcwd())
    script.create_new_day()