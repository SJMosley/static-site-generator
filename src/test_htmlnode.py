import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_html_eq(self):
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
    def test_html_not_eq(self):
        node1 = HTMLNode("p", "Some words")
        node2 = HTMLNode("a", "Wildflowers", None, {
            "href": "https://www.wildflower.org/texas-top-20",
            "target": "_blank",
        })
        self.assertNotEqual(node1, node2)
    def test_html_none(self):
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
    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "Hello Dad!")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>Hello Dad!</span></div>")
    def test_parent_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")
    def test_parent_to_html_children_none(self):
        parent_node = ParentNode("div", None)
        self.assertIsNotNone(parent_node.children)
    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "Hi Granddad!")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>Hi Granddad!</b></span></div>")
    def test_parent_eq(self):
        grandchild_node = LeafNode("b", "Hi Granddad!")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [
            ParentNode("span", [
                LeafNode("b", "Hi Granddad!")
            ])
        ])
        self.assertEqual(parent_node, parent_node2)
    def test_parent_not_eq(self):
        grandchild_node = LeafNode("b", "Hi Granddad!")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [
            LeafNode("span", "Hi Dad!")
        ])
        self.assertNotEqual(parent_node, parent_node2)

    def test_leaf_eq(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node1, node2)
    def test_leaf_not_eq(self):
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
