from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        #guard against children being none
        temp_children = children if children is not None else []
        super().__init__(tag, None, temp_children, props)
    def __repr__(self):
        has_children = "Yes" if self.children is not None else "No"
        return f"ParentNode({self.tag}, children:{has_children}, {self.props})"
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have a list of children (even if it's empty)")
        result_html = f"<{self.tag}{self.props_to_html()}>"
        end_tag = f"</{self.tag}>"

        if isinstance(self.children, LeafNode):
            return result_html + self.children.to_html() + end_tag
        for child in self.children:
            result_html += child.to_html()
        result_html += end_tag #add closing tag
        return result_html

# node = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )
# node2 = ParentNode(
#     "p",
#     None,
# )
# # print(node.to_html())
# print(node2.to_html())
