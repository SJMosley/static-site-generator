import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from markdown_to_html import markdown_to_html_node

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        goal = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        blocks = markdown_to_blocks(md)
        # print(f"blocks {blocks}")
        # print(f"answer {goal}")
        self.assertEqual(
            blocks,
            goal,
        )
    def test_block_to_block_type_paragraph(self):
        block = "This is **bolded** paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type
        )

    def test_block_to_block_type_heading(self):
        block = "# This is a heading 1"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.HEADING,
            block_type
        )
        block = "## This is a heading 2"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.HEADING,
            block_type
        )
        block = "### This is a heading 3"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.HEADING,
            block_type
        )
        block = "#### This is a heading 4"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.HEADING,
            block_type
        )
        block = "##### This is a heading 5"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.HEADING,
            block_type
        )
        block = "###### This is a heading 6"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.HEADING,
            block_type
        )

    def test_block_to_block_type_code(self):
        block = "```<div>\n\t<p>WORDS</p> \n</div>```"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.CODE,
            block_type
        )
    def test_block_to_block_type_quote(self):
        block = "> I can never tell a lie \n> - Ronald Reagan"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.QUOTE,
            block_type
        )
    def test_block_to_block_type_unordered_list(self):
        block = "- LIST ITEM 1\n- LIST ITEM 2\n- LIST ITEM 3"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_type
        )
    def test_block_to_block_type_ordered_list(self):
        block = "1. Cool\n2. beans\n3. Noice!"
        block_type = block_to_block_type(block)
        self.assertEqual(
            BlockType.ORDERED_LIST,
            block_type
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print("\n🚨🚨🚨")
        # print(f"n  {html}")
        # print(f'g <div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>')
        # print("\n🚨🚨🚨")
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        # print("\n🚨🚨🚨")
        # print(f"n  {html}")
        # print(f'g <div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>')
        # print("\n🚨🚨🚨")
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
