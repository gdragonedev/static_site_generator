import re

from htmlnode import HTMLNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    children = []

    for block in md_blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            children.append(p_block_to_html_node(block))
        elif block_type == block_type_heading:
            children.append(h_block_to_html_node(block))
        elif block_type == block_type_code:
            children.append(code_block_to_html_node(block))
        elif block_type == block_type_quote:
            children.append(quote_block_to_html_node(block))
        elif block_type == block_type_unordered_list:
            children.append(ul_block_to_html_node(block))
        elif block_type == block_type_ordered_list:
            children.append(ol_block_to_html_node(block))

    return HTMLNode("div", children=children)

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

def p_block_to_html_node(block):
    return HTMLNode("p", block)

def code_block_to_html_node(block):
    code_content = block.strip("` \n")
    code_node = HTMLNode("code", code_content)
    return HTMLNode("pre", [code_node])

def quote_block_to_html_node(block):
    quote_lines = block.split("\n")
    new_block = ""
    for line in quote_lines:
        new_block += f"{line.lstrip(">")}\n"

    return HTMLNode("blockquote", new_block)

def h_block_to_html_node(block):
    h_size = block.count("#", 0, block.index(" "))

    return HTMLNode(f"h{h_size}", block.lstrip("# "))

def ul_block_to_html_node(block):
    list_lines = block.split("\n")
    list_items = []
    for line in list_lines:
        list_items.append(HTMLNode("li", line.lstrip("*- ")))

    return HTMLNode("ul", children=list_items)

def ol_block_to_html_node(block):
    list_lines = block.split("\n")
    list_items = []
    for i in range(1, len(list_lines)):
        list_items.append(HTMLNode("li", list_lines[i].lstrip(f"{i}. ")))

    return HTMLNode("ol", children=list_items)