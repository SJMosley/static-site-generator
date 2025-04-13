
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
