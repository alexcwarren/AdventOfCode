from argparse import ArgumentParser
from os import getcwd, mkdir, path
from re import search, sub
from shutil import copy

from bs4 import BeautifulSoup
from requests import get as get_response

from markdown_converter.markdown_converter import MarkdownConverter


class DayCreator:
    """A class to create all necessary folder and files to work on given an
    \"Advent of Code\" Day Problem.
    """

    class __REPLACEMENTS:
        """
        A class to provide consistent values to replace text in copied template files.
        """

        PROBLEM_NAME: str = "REPLACE_WITH_PROBLEM_NAME"
        CLASS_NAME: str = "REPLACE_WITH_CLASS_NAME"
        DAY_NUMBER: str = "REPLACE_WITH_DAY_NUMBER"
        TITLE: str = "REPLACE_WITH_TITLE"
        URL: str = "REPLACE_WITH_URL"
        DESCRIPTION: str = "REPLACE_WITH_DESCRIPTION"

    def __init__(self, current_directory: str):
        """Set self.__current_dir to current_directory argument.

        Set self.__templates_dir to templates directory within self.__current_dir.

        Process command-line arguments.
        """
        self.__current_dir: str = current_directory
        self.__templates_dir: str = f"{self.__current_dir}/templates"
        self.__process_arguments()

    def create_new_day(self):
        """ "Retrieve Day data and create its directories and files."""
        self.__download_url_data()
        self.__check_year_directory()
        self.__create_day_directory()
        self.__create_files()

    def __process_arguments(self):
        """Process command-line arguments."""
        BASE_URL: str = "https://adventofcode.com"
        parser = ArgumentParser(
            prog="create_day.py",
            usage="python create_day.py [-y <year> -d <day>] [--url <AdventOfCode.com URL>]",
        )
        parser.add_argument(
            "-y", "--year", choices=[str(yr) for yr in range(2015, 2023)]
        )
        parser.add_argument("-d", "--day", choices=[str(dy) for dy in range(1, 26)])
        parser.add_argument("-u", "--url", default=BASE_URL)
        args = parser.parse_args()

        if args.url == BASE_URL:
            if not (args.year or args.day):
                parser.error(
                    'No arguments provided. Provide "year" and "day" or "url".'
                )
            self.__url: str = f"{BASE_URL}/{args.year}/day/{args.day}"
        else:
            self.__url: str = str(args.url).lower()
        if "adventofcode.com" not in self.__url:
            parser.error(f'{self.__url}: Please provide "adventofcode.com" URL.')

    def __download_url_data(self):
        """Retrieve HTML content from self.__url."""
        response = get_response(self.__url)
        self.__html_content = BeautifulSoup(response.content, "html.parser")
        self._year: str = self.__get_year()
        (
            self.__problem_title,
            self.__day_number,
            self.__problem_name,
        ) = self.__get_problem_header()
        self.__class_name: str = (
            self.__problem_name.replace("_", " ").title().replace(" ", "")
        )
        self.__problem_description: str = self.__get_problem_description()

    def __get_year(self) -> str:
        """Extract year from previously downloaded HTML content."""
        header = self.__html_content.find("h1", attrs={"class": "title-event"})
        year = search(r".*(\d{4}).*", header.text)
        return year.group(1)

    def __get_problem_header(self) -> tuple[str]:
        """Extract problem header info from previously downloaded HTML content."""
        problem_header: str = self.__html_content.find("h2").text.strip()
        day_match = search(r"\d", problem_header)
        title_match = search(r": (.+) -", problem_header)
        title: str = self.__convert_to_filename(title_match.group(1))
        return (sub(r" ?--- ?", "", problem_header), day_match.group(), title)

    def __get_problem_description(self) -> tuple:
        """Extract problem description from previously downloaded HTML content."""
        article_html = self.__html_content.find("article")
        return MarkdownConverter(self.__url).get_markdown(article_html)

    def __convert_to_filename(self, text: str) -> str:
        """Return text in its snakecase form."""
        return text.lower().replace(" ", "_")

    def __check_year_directory(self):
        """Check that year directory exists - create it if it doesn't."""
        self.__year_dir: str = f"{self.__current_dir}/{self._year}"
        if not path.isdir(self.__current_dir):
            mkdir(self.__year_dir)

    def __create_day_directory(self):
        """Create day directory within year directory.
        Raise exception if it exists already.
        """
        self.__day_dir: str = f"{self.__year_dir}/Day {self.__day_number}"
        try:
            mkdir(self.__day_dir)
        except Exception as exception:
            print(exception)
            exit()

    def __create_files(self):
        """Create all Day files."""
        self.__create_python_file()
        self.__create_markdown_file()
        self.__create_sample_data_file()
        self.__create_input_data_file()
        self.__create_python_test_file()

    def __create_python_file(self):
        """Copy template.py into Day directory and replace content with this Day's info."""
        python_file: str = f"{self.__day_dir}/{self.__problem_name}.py"
        copy(f"{self.__templates_dir}/template.py", python_file)

        file_contents: str = self.__get_file_contents(python_file)
        file_contents = (
            file_contents.replace(self.__REPLACEMENTS.CLASS_NAME, self.__class_name)
            .replace(self.__REPLACEMENTS.PROBLEM_NAME, self.__problem_name)
            .replace(self.__REPLACEMENTS.DAY_NUMBER, self.__day_number)
        )

        self.__write_file_contents(file_contents, python_file)

    def __create_markdown_file(self):
        """Copy Outline.md into Day directory and replace content with this Day's info."""
        outline_file: str = f"{self.__day_dir}/Outline.md"
        copy(f"{self.__templates_dir}/Outline.md", outline_file)

        file_contents: str = self.__get_file_contents(outline_file)
        file_contents = (
            file_contents.replace(self.__REPLACEMENTS.TITLE, self.__problem_title)
            .replace(self.__REPLACEMENTS.URL, self.__url)
            .replace(self.__REPLACEMENTS.DESCRIPTION, self.__problem_description)
        )

        self.__write_file_contents(file_contents, outline_file)

    def __get_file_contents(self, filepath: str) -> str:
        """Return contents of provided filepath."""
        file_contents = None
        with open(filepath, "r") as read_file:
            file_contents = read_file.read()
        return file_contents

    def __write_file_contents(self, file_contents: str, filepath: str):
        """Write provided file contents to provided filepath."""
        with open(filepath, "w") as write_file:
            write_file.write(file_contents)

    def __create_sample_data_file(self):
        """Create empty sample.in file in Day directory."""
        self.__create_empty_file("sample.in")

    def __create_empty_file(self, filename: str):
        """Create empty file in Day directory with provided filename."""
        self.__write_file_contents("", f"{self.__day_dir}/{filename}")

    def __create_input_data_file(self):
        """Create empty input.in file in Day directory."""
        self.__create_empty_file("input.in")

    def __create_python_test_file(self):
        """Copy test.py into Day directory and replace content with this Day's info."""
        test_file: str = f"{self.__day_dir}/test_{self.__problem_name}.py"
        copy(f"{self.__templates_dir}/test.py", test_file)

        file_contents: str = self.__get_file_contents(test_file)
        file_contents = file_contents.replace(
            self.__REPLACEMENTS.PROBLEM_NAME, self.__problem_name
        ).replace(self.__REPLACEMENTS.CLASS_NAME, self.__class_name)

        self.__write_file_contents(file_contents, test_file)


if __name__ == "__main__":
    script = DayCreator(getcwd())
    script.create_new_day()
