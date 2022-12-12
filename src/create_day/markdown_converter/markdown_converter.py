from os import getcwd
from re import match, sub

from bs4 import BeautifulSoup
from markdownify import markdownify


class MarkdownConverter:
    """A class for converting HTML to Markdown.

    Specifically used for \"Advent of Code\" Problem Descriptions.
    """

    def __init__(self, url: str = "https://adventofcode.com"):
        """Set `url` to what is provided or \"https://adventofcode.com\" if not provided.

        Set `input_file` to html.txt.

        Set `output_file` to markdown.md.
        """
        self.url: str = url
        self.intput_file: str = f"{getcwd()}/html.txt"
        self.output_file: str = f"{getcwd()}/markdown.md"

    def get_markdown(self, html) -> str:
        """Return string of all HTML elements converted to Markdown."""
        return "".join(self.get_markdown_element(element) for element in html).strip()

    def get_markdown_element(self, element) -> str:
        """Return Markdown string for each element.

        Ignore empty lines and `<h2>` tags.

        Correct incomplete href attributes in `<a>` tags.

        Fix order of non-word character and asterisk for emphasized text.

        Replace italic with strong emphasis.

        Fix extra new-line in code blocks.
        """
        element_str = str(element)
        if match(r"\s+", element_str) or "h2" in element_str:
            return ""

        elif "href" in element_str and element_str.startswith("/"):
            element_str = sub(r"href=\"(.+)\"", f'href="{self.url}\\g<1>"', element_str)

        markdown_element = markdownify(
            element_str, heading_style="ATX", bullets="-", code_language="python"
        ).strip()

        # Correct order of non-word character and * characters in text
        markdown_element = sub(
            r"(\S)(\*+)(\w+)(\*+)(\S)", r"\g<2>\g<1>\g<3>\g<5>\g<4>", markdown_element
        )

        # Replace italic with strong emphasis
        # Remove extra newline in code blocks
        markdown_element = f"{markdown_element}\n\n".replace("*", "**").replace(
            "\n```\n", "```\n"
        )
        return markdown_element

    def write_markdown(self):
        """Write retrieved Markdown string (via html.txt) to markdown.md."""
        html: str = None
        with open(self.intput_file, "r") as read_file:
            html = read_file.read()
        with open(self.output_file, "w") as write_file:
            write_file.write(self.get_markdown(BeautifulSoup(html, "html.parser")))


if __name__ == "__main__":
    script = MarkdownConverter()
    script.write_markdown()
