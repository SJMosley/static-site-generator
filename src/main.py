from textnode import TextNode, TextType
from build_site import publish_content
from generate import generate_page
def main():
    copy_from_dir = './static' #from_dir
    dest_dir = './public' #to_dir
    content_file = './content/index.md'
    template_file =  './template.html'
    dest_file = './public/index.html'

    publish_content(copy_from_dir, dest_dir)
    generate_page(content_file, template_file,dest_file)

main()
