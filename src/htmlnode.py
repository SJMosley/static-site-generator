
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def __eq__(self, other):
        eq_tag = self.tag == other.tag
        eq_value = self.value == other.value
        eq_children = self.children == other.children
        eq_props = self.props == other.props
        return eq_tag and eq_value and eq_children and eq_props
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if not self.props:
            return ""

        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html


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


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
# print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())
# print(LeafNode("p", "This is a paragraph of text.").to_html())
