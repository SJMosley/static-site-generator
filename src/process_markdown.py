from enum import Enum
from inline_markdown import text_to_text_nodes
from textnode import text_node_to_html_node, TextNode, TextType
from htmlnode import ParentNode

def markdown_to_blocks(md):
    # print(f"md {md}")

    starting_blocks = md.split('\n\n')
    result_blocks = []
    for block in starting_blocks:
        if len(block) == 0:
            continue
        result_blocks.append(block.strip())

    return result_blocks

    # print(f"blocks {blocks}")

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    headings_tuple = ("# ","## ", "### ","#### ", "##### ", "###### ")
    if block.startswith(headings_tuple):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def extract_title(md):
    lines = md.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("no header!")

def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    nodes = []
    for block in blocks:
        html_node = block_to_html_node(block)
        nodes.append(html_node)
    return ParentNode("div", nodes, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")

def paragraph_to_html_node(block):
    clean_text = block.replace("\n", " ")
    children = text_to_children(clean_text)
    return ParentNode("p", children)

def heading_to_html_node(block):
    heading_tag, heading_num = get_heading_tag(block)
    children = text_to_children(block[heading_num:].strip())
    return ParentNode(heading_tag, children)

def get_heading_tag(text):
    md_heading = text.split()[0]
    heading_num = len(md_heading)
    return (f"h{heading_num}", heading_num)

def unordered_list_to_html_node(block):
    children = []
    lines = block.split('\n')
    for line in lines:
        line_children = text_to_children(line[2:])
        html_node = ParentNode("li", line_children)
        children.append(html_node)
    return ParentNode("ul", children)

def ordered_list_to_html_node(block):
    children = []
    lines = block.split('\n')
    for line in lines:
        num_index = line.find(". ") + 2 # add 2 for the sub of characters.
        line_children = text_to_children(line[num_index:])
        html_node = ParentNode("li", line_children)
        children.append(html_node)
    return ParentNode("ol", children)

def quote_to_html_node(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    joined_lines = " ".join(new_lines)
    children = text_to_children(joined_lines)
    return ParentNode("blockquote", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
            raise ValueError("invalid code block")
    text = block[4:-3] #cut out the tick marks
    text_node = TextNode(text, TextType.TEXT)
    children = text_node_to_html_node(text_node)
    code_node = ParentNode("code", [children])
    return ParentNode("pre", [code_node])

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes
