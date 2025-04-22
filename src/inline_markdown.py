import re
from textnode import TextNode, TextType

def text_to_text_nodes(text):
    # print("\n🚨🚨🚨")
    # print(f"nodes \n{nodes}")
    nodes = [TextNode(text, TextType.TEXT, None)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
#This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

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

def split_nodes_logic(extraction_func, old_nodes, extracted_node_type=None):
    #Same logic for image and link functions, pulling it out
    #Extraction func must return Tuple of (text, url)
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        current_text = old_node.text
        extracted_items = extraction_func(current_text)
        if extracted_items == []:
            new_nodes.append(old_node)
            continue
        for text, url in extracted_items:
            if extracted_node_type == TextType.IMAGE:
                item_delim = f"![{text}]({url})"
            elif extracted_node_type == TextType.LINK:
                item_delim = f"[{text}]({url})"
            else:
                raise Exception("no delimiter for type provided")

            left, item, right = current_text.partition(item_delim)
            if left != "":
                split_nodes.append(TextNode(left, TextType.TEXT))
            if item:
                split_nodes.append(TextNode(text, extracted_node_type, url))
            if right or right == "":
                current_text = right
        if current_text != "":
            split_nodes.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes_logic(extract_markdown_images, old_nodes, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes_logic(extract_markdown_links, old_nodes, TextType.LINK)

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

#Printed Tests from the lesson
# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
#
# print("\n🚨🚨🚨")
# node = TextNode(
#         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
#         TextType.TEXT,
#     )
# print(split_nodes_image([node]))
# print("\n🚨🚨🚨")
# linknode = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# print(split_nodes_link([linknode]))
# print("\n🚨🚨🚨")
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
