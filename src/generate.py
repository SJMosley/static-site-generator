import os
from process_markdown import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, destination_path):
    print(f"Generating page {from_path} to {destination_path}, using {template_path}")

    with open(from_path) as md_file:
        markdown = md_file.read()
        # md_file.close()
    with open(template_path) as template_file:
        template = template_file.read()
        # template_file.close()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    result_html = template.replace("{{ Content }}", content)
    print(template)

    #destination_path and making dirs
    print(f"dest_path {destination_path}")
    dest_dir_name = os.path.dirname(destination_path)
    print(f"dest_dir_name {dest_dir_name}")
    if not os.path.exists(dest_dir_name):
        os.makedirs(dest_dir_name)

    with open(destination_path, 'w') as destination_file:
        destination_file.write(result_html)
