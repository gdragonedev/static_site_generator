import re

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

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

    return ParentNode("div", children=children)

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

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def p_block_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def code_block_to_html_node(block):
    text = block.strip("` \n")
    children = text_to_children(text)
    code_node = ParentNode("code", children)
    return ParentNode("pre", [code_node])

def quote_block_to_html_node(block):
    quote_lines = block.split("\n")
    new_block = ""
    for line in quote_lines:
        new_block += f"{line.lstrip("> ")}"
    text = new_block
    children = text_to_children(text)
    
    return ParentNode("blockquote", children)

def h_block_to_html_node(block):
    h_size = block.count("#", 0, block.index(" "))
    text = block.lstrip("# ")
    children = text_to_children(text)

    print(f"children: {children}")

    return ParentNode(f"h{h_size}", children)

def ul_block_to_html_node(block):
    list_lines = block.split("\n")
    list_items = []
    for line in list_lines:
        text = line.lstrip("*- ")
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))

    return ParentNode("ul", list_items)

def ol_block_to_html_node(block):
    list_lines = block.split("\n")
    list_items = []
    for line in list_lines:
        text = line[3:]
        children = text_to_children(text)
        list_items.append(ParentNode("li", children))

    return ParentNode("ol", list_items)