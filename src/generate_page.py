import os
from pathlib import Path
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    if os.path.isfile(markdown):
        with open(markdown, "r") as file:
            lines = file.readlines()
    else:
        lines = markdown.splitlines()

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError(f"Title not found in provided markdown content.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'")

    with open(from_path, "r") as data:
        content = data.read()

    with open(template_path, "r") as data:
        template = data.read()

    node = markdown_to_html_node(content)
    html_content = node.to_html()
    template = template.replace("{{ Title }}", extract_title(content))
    template = template.replace("{{ Content }}", html_content)

    dir = os.path.dirname(dest_path)
    if dir:
        os.makedirs(dir, exist_ok=True)

    with open(dest_path, "w") as data:
        data.write(template)
    
    print(f"Page generated.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        content_file_path = os.path.join(dir_path_content, item)
        dest_file_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(content_file_path):
            dest_file_path = Path(dest_file_path).with_suffix(".html")
            generate_page(content_file_path, template_path, dest_file_path)
        else:
            os.makedirs(dest_file_path, exist_ok=True)
            generate_pages_recursive(content_file_path, template_path, dest_file_path)
