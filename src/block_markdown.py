import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

def markdown_to_blocks(markdown):
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, markdown.strip())

def block_to_block_type(md_block):
    md_lines = re.split("\n", md_block.strip())

    #heading
    if re.match(r"^#{1,6} ", md_block):
        return block_type_heading
    
    #code
    if md_block.startswith("```") and md_block.endswith("```"):
        return block_type_code
    
    #quote
    if all(line.startswith(">") for line in md_lines):
        return block_type_quote
    
    #unordered list
    if all(line.startswith("* ") for line in md_lines) or all(line.startswith("- ") for line in md_lines):
        return block_type_unordered_list
    
    #ordered list
    block_is_ol = True
    for i, line in enumerate(md_lines, start=1):
        if not line.startswith(f"{i}. "):
            block_is_ol = False
            break
    if block_is_ol:
        return block_type_ordered_list
    
    return block_type_paragraph