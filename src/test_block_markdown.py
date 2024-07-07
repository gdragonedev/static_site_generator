import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        
        block_strings = [
                            "This is **bolded** paragraph",
                            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                            "* This is a list\n* with items"
                        ]
        self.assertListEqual(markdown_to_blocks(markdown), block_strings)

    def test_markdown_to_blocks_newlines(self):
        markdown = """
This is **bolded** paragraph






This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line




* This is a list
* with items"""
        
        block_strings = [
                            "This is **bolded** paragraph",
                            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                            "* This is a list\n* with items"
                        ]
        self.assertListEqual(markdown_to_blocks(markdown), block_strings)

    def test_block_to_block_type_paragraph(self):
        md_block = "This is a simple paragraph block, which does not start with any specific markdown characters."

        self.assertEqual(block_to_block_type(md_block), block_type_paragraph)

    def test_block_to_block_type_heading(self):
        md_block = "## This is a heading block"

        self.assertEqual(block_to_block_type(md_block), block_type_heading)

    def test_block_to_block_type_code(self):
        md_block = """```
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"
```"""

        self.assertEqual(block_to_block_type(md_block), block_type_code)

    def test_block_to_block_type_quote(self):
        md_block = """
> This is a quote block.
> It spans multiple lines."""

        self.assertEqual(block_to_block_type(md_block), block_type_quote)

    def test_block_to_block_type_quote_mixed(self):
        md_block = """
>This is a quote block.
> It spans multiple lines."""

        self.assertEqual(block_to_block_type(md_block), block_type_quote)

    def test_block_to_block_type_unordered_list(self):
        md_block = """
* Item 1
* Item 2
* Item 3"""

        self.assertEqual(block_to_block_type(md_block), block_type_unordered_list)

    def test_block_to_block_type_unordered_list_mixed(self):
        md_block = """
* Item 1
- Item 2
* Item 3"""

        self.assertNotEqual(block_to_block_type(md_block), block_type_unordered_list)

    def test_block_to_block_type_ordered_list(self):
        md_block = """
1. First item
2. Second item
3. Third item"""

        self.assertEqual(block_to_block_type(md_block), block_type_ordered_list)

    def test_block_to_block_type_ordered_list_syntax(self):
        md_block = """
1. First item
II. Second item
3. Third item"""

        self.assertNotEqual(block_to_block_type(md_block), block_type_ordered_list)

    def test_block_to_block_types(self):    
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()
