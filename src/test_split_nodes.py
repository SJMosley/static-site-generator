import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestSplitTextNode(unittest.TestCase):
    def test_split_text_no_inline(self):
        node = TextNode("This is a text block with no splitter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [TextNode("This is a text block with no splitter", TextType.TEXT)]
        )
    def test_split_bad_delimiter(self):
        node = TextNode("This is a text block with no splitter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "!", TextType.CODE)
    def test_split_not_closed(self):
        node = TextNode("This is a **fucked test block", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    def test_split_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )
    def test_split_double(self):
        node = TextNode("This is **double bold text** with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("double bold text", TextType.BOLD),
                TextNode(" with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )
    def test_split_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic block", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ]
        )
    def test_split_bold_and_italic(self):
        node = TextNode("This is text with an _italic_ word and a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )
    def test_split_code(self):
        node = TextNode("This is text with a Code Block `<div></div>` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a Code Block ", TextType.TEXT),
                TextNode("<div></div>", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
    # def test_split_link(self):
    # def test_split_image(self):


# Normal text/Text
# **Bold text**
# _Italic text_
# `Code text`
# Links, in this format: [anchor text](url)
# Images, in this format: ![alt text](url)
