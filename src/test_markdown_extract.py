import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)

class TestMarkdownExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([('link', 'https://i.imgur.com/zjjcJKZ.png')], matches)
    def test_multiple_extract_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) And this beutiful ![climbing pic](https://unsplash.com/photos/person-in-red-jacket-and-blue-pants-sitting-on-rock-mountain-covered-with-snow-during-daytime-m6wbWMF6p9s)"
        )
        self.assertListEqual([
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("climbing pic",
                "https://unsplash.com/photos/person-in-red-jacket-and-blue-pants-sitting-on-rock-mountain-covered-with-snow-during-daytime-m6wbWMF6p9s"
            )
        ], matches)
