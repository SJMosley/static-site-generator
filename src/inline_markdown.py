import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in "_**`":
        raise ValueError(f"invalid delimiter: {delimiter}")
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(f"invalid markdown. No matching delimiter.\nCheck source text{old_node.text}")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], old_node.text_type))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    #NON RECURSIVE
    return new_nodes

def simple_markdown_extract(pattern, text):
    return re.findall(pattern, text)

def extract_markdown_images(text):
    return simple_markdown_extract(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return simple_markdown_extract(r"\[(.*?)\]\((.*?)\)", text)

#Printed Tests from the lesson
# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
