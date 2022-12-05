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
from requests import get as get_response
from bs4 import BeautifulSoup
from re import search, match, sub, findall
from os import getcwd, mkdir, path
from shutil import copy
from markdownify import markdownify


class DayCreator:
    def __init__(self, current_directory: str):
        self.current_dir: str = current_directory
        self.templates_dir: str = f"{self.current_dir}/templates"
        self.process_arguments()

    def create_new_day(self):
        self.get_url_data()
        # self.check_year_directory()
        # self.create_day_directory()
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
        response = get_response(self.url)
        self.html_content = BeautifulSoup(response.content, "html.parser")
        self.year: str = self.get_year()
        self.day_number, self.problem_name = self.get_problem_header()
        self.problem_title, self.problem_description = self.get_problem_description()

    def get_year(self) -> str:
        header = self.html_content.find("h1", attrs={"class": "title-event"})
        year = search(r".*(\d{4}).*", header.text)
        return year.group(1)

    def get_problem_header(self) -> tuple[str]:
        problem_header: str =  self.html_content.find("h2").text.strip()
        day_match = search(r"\d", problem_header)
        title_match = search(r": (.+) -", problem_header)
        title: str = self.convert_to_filename(title_match.group(1))
        return (day_match.group(), title)

    def get_problem_description(self) -> tuple:
        article_html = self.html_content.find("article")
        title: str = ""
        description: str = ""
        for element in article_html:
            element_str: str = str(element)
            is_title: bool = False
            if match(r"\s+", element_str):
                continue

            if "h2" in element_str:
                is_title = True
                element_str = element_str.replace("h2", "")
                element_str = element_str.replace("<>", "").replace("</>", "")

            elif "href" in element_str:
                element_str = sub(
                    r"href=\"(.+)\"", f"href=\"{self.url}\\g<1>\"", element_str
                )

            element_markdown = markdownify(
                element_str,
                heading_style="ATX",
                bullets="-",
                code_language="python"
            ).strip()

            em_code_elements: list = findall(r"`\*\d+\*`", element_markdown)
            if em_code_elements:
                for element in em_code_elements:
                    digits_search: str = search(r"\d+", element)
                    element_markdown = element_markdown.replace(
                        element, f"*`{digits_search.group()}`*"
                    )

            if is_title:
                title = element_markdown
            else:
                description += f"{element_markdown}\n\n"

        return (title, description.strip().replace("*", "**").replace("\n```\n", "```\n"))

    def convert_to_filename(self, text: str) -> str:
        return text.lower().replace(" ", "_")

    def check_year_directory(self):
        self.year_dir: str = f"{self.current_dir}/{self.year}"
        if not path.isdir(self.current_dir):
            mkdir(self.year_dir)

    def create_day_directory(self):
        self.day_dir: str = f"{self.year_dir}/Day {self.day_number}"
        try:
            mkdir(self.day_dir)
        except:
            print(
                f"ERROR: directory \"{self.day_dir}\" already exists."
            )
            exit()

    def create_files(self):
        self.create_python_file()
        # self.create_markdown_file()
        # self.create_sample_data_file()
        # self.create_input_data_file()
        # self.create_python_test_file()

    def create_python_file(self):
        # python_file: str = f"{self.day_dir}/{self.problem_name}.py"
        python_file: str = f"{self.current_dir}/{self.problem_name}.py"
        # copy(
        #     f"{self.templates_dir}/template.py",
        #     python_file
        # )
        
    
    def create_markdown_file(self):
        outline_file: str = f"{self.day_dir}/Outline.md"
        copy(f"{self.templates_dir}/Outline.md", outline_file)

        file_contents = None
        with open(outline_file, "r") as read_file:
            file_contents = read_file.read()

        file_contents = file_contents.replace("REPLACE_WITH_TITLE", self.problem_title).replace("REPLACE_WITH_URL", self.url).replace("REPLACE_WITH_DESCRIPTION", self.problem_description)

        with open(outline_file, "w") as write_file:
            write_file.write(file_contents)
    
    def create_sample_data_file(self):
        self.create_empty_file("sample.in")

    def create_empty_file(self, filename: str):
        with open(f"{self.day_dir}/{filename}", "w") as file:
            file.write("")
    
    def create_input_data_file(self):
        self.create_empty_file("input.in")
    
    def create_python_test_file(self):
        copy(
            f"{self.templates_dir}/test.py",
            f"{self.day_dir}/test_{self.problem_title}.py"
        )


if __name__ == "__main__":
    script = DayCreator(getcwd())
    script.create_new_day()