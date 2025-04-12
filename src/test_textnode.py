import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node = TextNode("This is a text node", TextType.BOLD, "https://www.wildflower.org/texas-top-20")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.wildflower.org/texas-top-20")
        self.assertEqual(node, node2)
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(None, node.url)
    def test_not_eq_text(self):
        node = TextNode("This is a word node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.wildflower.org/texas-top-20")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://news.ycombinator.com/")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
