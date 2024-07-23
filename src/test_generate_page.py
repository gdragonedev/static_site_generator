import unittest
from generate_page import extract_title

def test_extract_title(self):
    markdown = """
Some introductory text
# Hello World
More text
"""
    self.assertEqual(extract_title(markdown), "Hello World")

def test_extract_title_wrong_heading(self):
    markdown = """
Some introductory text
## Hello World
More text
"""
    self.assertNotEqual(extract_title(markdown), "Hello World")

def test_extract_title_no_heading(self):
    markdown = """
Some introductory text
Hello World
More text
"""
    self.assertNotEqual(extract_title(markdown), "Hello World")

def test_extract_title_file(self):
    markdown = "/content/index.md"
    self.assertEqual(extract_title(markdown), "Tolkien Fan Club")