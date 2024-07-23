import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def text_to_textnodes(text):
    #cast input text as TextNode, and run splitters that require only [node] params
    new_nodes = split_nodes_image(split_nodes_link([TextNode(text, text_type_text, None)]))

    delimiters = [
        ("**", text_type_bold),
        ("*", text_type_italic),
        ("`", text_type_code),
    ]
    for delim in delimiters:
        new_nodes = split_nodes_delimiter(new_nodes, delim[0], delim[1])

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    if text == '' or text == None:
        raise ValueError("Invalid: Cannot extract images from empty/None text")
    
    regex = r"!\[(.*?)\]\((.*?)\)"

    return re.findall(regex, text) or [None]

def extract_markdown_links(text):
    if text == '' or text == None:
        raise ValueError("Invalid: Cannot extract links from empty/None text")
    
    regex = r"(?<!\!)\[(.*?)\]\((.*?)\)"

    return re.findall(regex, text) or [None]

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        img_tuples = extract_markdown_images(old_node.text)
        if img_tuples == [None]:
            new_nodes.append(old_node)
            continue

        string_to_split = old_node.text
        split_nodes = []
        for img_tup in img_tuples:
            sections = string_to_split.split(f"![{img_tup[0]}]({img_tup[1]})", 1)
            if sections[0]:
                split_nodes.append(TextNode(sections[0], text_type_text))

            split_nodes.append(TextNode(img_tup[0], text_type_image, img_tup[1]))

            if len(sections) > 1:
                string_to_split = sections[1]
            else:
                string_to_split = ""

        if string_to_split:
            split_nodes.append(TextNode(string_to_split, text_type_text))

        new_nodes.extend(split_nodes)

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        link_tuples = extract_markdown_links(old_node.text)
        if link_tuples == [None]:
            new_nodes.append(old_node)
            continue

        string_to_split = old_node.text
        split_nodes = []
        for link_tup in link_tuples:
            sections = string_to_split.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if sections[0]:
                split_nodes.append(TextNode(sections[0], text_type_text))

            split_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))

            if len(sections) > 1:
                string_to_split = sections[1]
            else:
                string_to_split = ""

        if string_to_split:
            split_nodes.append(TextNode(string_to_split, text_type_text))

        new_nodes.extend(split_nodes)

    return new_nodes
