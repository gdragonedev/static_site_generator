from textnode import TextNode
from htmlnode import HTMLNode

def main():
    test_text = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(test_text)

    test_HTML = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com"})
    #print(test_HTML)

main()