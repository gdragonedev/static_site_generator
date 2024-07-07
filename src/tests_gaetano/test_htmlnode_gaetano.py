import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_node = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank"})
        props_html = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(test_node.props_to_html(), props_html)

class TestLeafNode(unittest.TestCase):
    def test_LeafNode_to_html(self):
        # First LeafNode without props
        test_leaf1 = LeafNode("p", "This is a paragraph of text.")
        leaf1_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(test_leaf1.to_html(), leaf1_html)
        
        # Second LeafNode with props
        test_leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leaf2_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(test_leaf2.to_html(), leaf2_html)

class TestParentNode(unittest.TestCase):
    def test_ParentNode_to_html(self):
        parent1_test = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        parent1_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(parent1_test.to_html(), parent1_html)
    
    def test_nested_ParentNode_to_html(self):
        parent2_test = ParentNode(
                            "p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                ParentNode(
                                    "p",
                                    [
                                        LeafNode("b", "Bold text"),
                                        LeafNode(None, "Normal text"),
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Normal text"),
                                    ],
                                ),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ],
                        )
        parent2_html = "<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>"
        self.assertEqual(parent2_test.to_html(), parent2_html)

    def test_nested_ParentNode_to_html(self):
        parent3_test = ParentNode(
                            "p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                ParentNode(
                                    "p",
                                    [
                                        LeafNode("b", "Bold text"),
                                        LeafNode(None, "Normal text"),
                                        ParentNode(
                                            "p",
                                            [
                                                LeafNode("b", "Bold text"),
                                                LeafNode(None, "Normal text"),
                                                ParentNode(
                                                    "p",
                                                    [
                                                        LeafNode("b", "Bold text"),
                                                        LeafNode(None, "Normal text"),
                                                        LeafNode("i", "italic text"),
                                                        LeafNode(None, "Normal text"),
                                                    ],
                                                ),
                                                LeafNode("i", "italic text"),
                                                LeafNode(None, "Normal text"),
                                            ],
                                        ),
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Normal text"),
                                    ],
                                ),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ],
                        )
        parent3_html = "<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><i>italic text</i>Normal text</p><i>italic text</i>Normal text</p><i>italic text</i>Normal text</p>"
        self.assertEqual(parent3_test.to_html(), parent3_html)

    

if __name__ == "__main__":
    unittest.main()