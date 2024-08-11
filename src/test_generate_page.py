import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
Some introductory text
# Hello World
More text"""
        self.assertEqual(extract_title(markdown), "Hello World")

if __name__ == "__main__":
    unittest.main()