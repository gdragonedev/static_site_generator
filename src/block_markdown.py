import re

def markdown_to_blocks(markdown):
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, markdown.strip())