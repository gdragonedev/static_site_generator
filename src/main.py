import os

from static_to_public import copy_static_recursive, clear_destination
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    
    if not os.path.exists(dir_path_static):
        print(f"Error: Source directory '{dir_path_static}' does not exist.")
        return
    if not os.path.exists(dir_path_public):
        os.makedirs(dir_path_public)
        print(f"Created destination directory '{dir_path_public}'.")
    
    try:
        clear_destination(dir_path_public)
        copy_static_recursive(dir_path_static, dir_path_public)
        print(f"Files copied from {dir_path_static} to {dir_path_public} successfully...")
    except Exception as e:
        print(f"Files not copied, error: {e}")

    generate_page(os.path.join(dir_path_content, "index.md"), template_path, os.path.join(dir_path_public, "index.html"))

if __name__ == "__main__":
    main()