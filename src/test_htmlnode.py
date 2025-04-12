import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        child = HTMLNode("p","This is the way")
        node1 = HTMLNode("p", None, None, None)
        node2 = HTMLNode("p", None, None, None)
        self.assertEqual(node1, node2)
        node1 = HTMLNode("p", "Some words", None, None)
        node2 = HTMLNode("p", "Some words", None, None)
        self.assertEqual(node1, node2)
        node1 = HTMLNode("p", "Some words", child, None)
        node2 = HTMLNode("p", "Some words", child, None)
        self.assertEqual(node1, node2)
        node1 = HTMLNode("p", "Some words", child, props)
        node2 = HTMLNode("p", "Some words", child, props)
        self.assertEqual(node1, node2)
    def test_not_eq(self):
        node1 = HTMLNode("p", "Some words")
        node2 = HTMLNode("a", "Wildflowers", None, {
            "href": "https://www.wildflower.org/texas-top-20",
            "target": "_blank",
        })
        self.assertNotEqual(node1, node2)
    def test_none(self):
        node = HTMLNode(value="Pretty Empty")
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        node = HTMLNode(tag="p")
        self.assertIsNone(node.value)

    def test_props_to_html(self):
        child = HTMLNode("p", "hackernews")
        node = HTMLNode(tag="a",children=child,props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        # print("\n🚨🚨🚨")
        # print(node)
        # print(node.props)
        # print(f"node_to_props {node.props_to_html()}")
        # print("🚨🚨🚨")
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())
