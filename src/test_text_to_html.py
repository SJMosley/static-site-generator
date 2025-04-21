import unittest
from textnode import TextNode, TextType, text_node_to_html_node
# from htmlnode import LeafNode, ParentNode

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("Hello Text World!", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello Text World!")
    def test_italic(self):
        node = TextNode("Hello Italian Text World!", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Hello Italian Text World!")
    #def test_bold
    def test_bold(self):
        node = TextNode("Hello Bold Text World!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Hello Bold Text World!")
    #def test_code
    #def test_link
    def test_image(self):
            node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "img")
            self.assertEqual(html_node.value, "")
            self.assertEqual(
                html_node.props,
                {"src": "https://www.boot.dev", "alt": "This is an image"},
            )
