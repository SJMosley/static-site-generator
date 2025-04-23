import sys
# from textnode import TextNode, TextType
from build_site import publish_content
from generate import generate_pages_recursive#, generate_page
def main():
    base_path = '/'
    if sys.argv[1]:
        base_path = sys.argv[1]

    copy_from_dir = './static' #from_dir
    dest_dir = './docs' #to_dir
    content_dir = './content'
    template_file =  './template.html'
    # content_file = './content/index.md'
    # dest_file = './public/index.html'

    publish_content(copy_from_dir, dest_dir)
    generate_pages_recursive(content_dir, template_file, dest_dir, base_path)
    #ORIGINAL# generate_pages_recursive(content_dir, template_file, dest_dir)
    # generate_page(content_file, template_file, dest_file)

main()
