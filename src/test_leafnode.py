import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1, node2)
    def test_not_eq(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(node1, node2)
    # def test_props_none(self):
    # def test_props(self):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")
    # def test_leaf_to_html_div(self):
    # def test_leaf_to_html_body(self):
    # def test_leaf_to_html_table(self):
    # def test_leaf_to_html_b(self):
    # def test_leaf_to_html_i(self):
    # def test_leaf_to_html_headers(self):
