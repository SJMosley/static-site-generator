from textnode import TextNode, TextType

def main():
    flower_node = TextNode("20 Wildflowers", TextType.LINK, "https://www.wildflower.org/texas-top-20")
    print(flower_node)

main()
