from enum import Enum

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            result_blocks.append(block)
    return result_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    headings_tuple = ("# ","## ", "### ","#### ", "##### ", "###### ")
    if block.startswith(headings_tuple):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def clean_block_md_text(text, block_type):
    cleaned_text = text.lstrip("# `>")
    cleaned_text = cleaned_text.rstrip("`")
    if block_type != BlockType.CODE:
        cleaned_text = cleaned_text.replace("\n", " ")
    # print(f"cleaned_text {cleaned_text}")
    return cleaned_text



#IN FILE Print TESTS
# markdown = """# This is a heading

# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.







# - This is the first list item in a list block
# - This is a list item
# - This is another list item"""

# print(f"markdown_to_blocks \n{markdown_to_blocks(markdown)}")

# md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """
# print(f"markdown_to_blocks \n{markdown_to_blocks(md)}")
