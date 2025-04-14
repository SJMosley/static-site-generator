import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "Hello Dad!")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>Hello Dad!</span></div>")
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")
    def test_to_html_children_none(self):
        parent_node = ParentNode("div", None)
        self.assertIsNotNone(parent_node.children)
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "Hi Granddad!")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>Hi Granddad!</b></span></div>")
    def test_eq(self):
        grandchild_node = LeafNode("b", "Hi Granddad!")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [
            ParentNode("span", [
                LeafNode("b", "Hi Granddad!")
            ])
        ])
        self.assertEqual(parent_node, parent_node2)
    def test_not_eq(self):
        grandchild_node = LeafNode("b", "Hi Granddad!")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [
            LeafNode("span", "Hi Dad!")
        ])
        self.assertNotEqual(parent_node, parent_node2)
