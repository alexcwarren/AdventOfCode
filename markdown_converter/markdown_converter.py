from os import getcwd
from re import findall, match, search, sub

from bs4 import BeautifulSoup
from markdownify import markdownify


class MarkdownConverter:
    def __init__(self):
        self.intput_file: str = f"{getcwd()}/html.txt"
        self.output_file: str = f"{getcwd()}/markdown.md"

    def get_markdown(self, html) -> str:
        return (
            "".join(self.get_markdown_element(element) for element in html).strip()
            + "\n"
        )

    def get_markdown_element(self, element) -> str:
        element_str = str(element)
        if match(r"\s+", element_str):
            return ""

        if "h2" in element_str:
            element_str = sub(r"<(/?)h2.*?>", r"<\g<1>h1>", element_str)
            element_str = element_str.replace("<>", "").replace("</>", "")

        elif "href" in element_str:
            element_str = sub(r"href=\"(.+)\"", f'href="{self.url}\\g<1>"', element_str)

        markdown_element = markdownify(
            element_str, heading_style="ATX", bullets="-", code_language="python"
        ).strip()

        em_code_elements: list = findall(r"`\*\d+\*`", markdown_element)
        if em_code_elements:
            for element in em_code_elements:
                digits_search: str = search(r"\d+", element)
                markdown_element = markdown_element.replace(
                    element, f"*`{digits_search.group()}`*"
                )
        markdown_element = f"{markdown_element}\n\n".replace("*", "**").replace(
            "\n```\n", "```\n"
        )
        return markdown_element

    def write_markdown(self):
        html: str = None
        with open(self.intput_file, "r") as read_file:
            html = read_file.read()
        with open(self.output_file, "w") as write_file:
            write_file.write(self.get_markdown(BeautifulSoup(html, "html.parser")))


if __name__ == "__main__":
    script = MarkdownConverter()
    script.write_markdown()
