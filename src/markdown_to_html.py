from block_markdown import markdown_to_blocks, BlockType, block_to_block_type, clean_block_md_text
from parentnode import ParentNode
from textnode import TextType, TextNode, text_node_to_html_node
from inline_markdown import text_to_text_nodes

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)

    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        nodes.append(build_node(block_type, block))

    parent_block = ParentNode("div", nodes)
    return parent_block

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)

    return html_nodes

def build_node(block_type, text):
    children = None
    # print(f"text {text}")
    cleaned_text = clean_block_md_text(text, block_type)
    if block_type != BlockType.CODE:
        children = text_to_children(cleaned_text)
    node = None
    match block_type:
        case BlockType.PARAGRAPH:
            node = ParentNode("p", children)
        case BlockType.HEADING:
            heading_tag = get_heading_tag(text)
            node = ParentNode(heading_tag, children)
        case BlockType.QUOTE:
            node = ParentNode("blockquote", children)
        case BlockType.UNORDERED_LIST:
            node = ParentNode("ul", children)
        case BlockType.ORDERED_LIST:
            node = ParentNode("ol", children)
        case BlockType.CODE:
            text_node = TextNode(cleaned_text.lstrip(), TextType.CODE)
            # print(f"text_node {text_node}")
            html_node = text_node_to_html_node(text_node)
            # print(f"html_node {html_node}")
            # print(f"html_node_to_html {html_node.to_html()}")
            node = ParentNode("pre", html_node)
        case _:
            raise ValueError("Not a valid block_type")
    return node

def get_heading_tag(text):
    md_heading = text.split()[0]
    heading_num = len(md_heading)
    return f"h{heading_num}"
