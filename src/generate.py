import os
from process_markdown import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, destination_path, base_path):
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
    template = template.replace("{{ Content }}", content)
    print("\n🚨🚨🚨")
    print(f"pre_href {template}")
    template = template.replace('href="/',f'href="{base_path}')
    print(f"post_href {template}")
    print(f"pre_src {template}")
    result_html = template.replace('src="/',f'src="{base_path}')
    print(f"post_src {result_html}")
    print("\n🚨🚨🚨")
    # print(template)

    #destination_path and making dirs
    # print(f"dest_path {destination_path}")
    dest_dir_name = os.path.dirname(destination_path)
    # print(f"dest_dir_name {dest_dir_name}")
    if not os.path.exists(dest_dir_name):
        os.makedirs(dest_dir_name)

    with open(destination_path, 'w') as destination_file:
        destination_file.write(result_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    dir_items = os.listdir(dir_path_content)
    for item in dir_items:
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isdir(item_path):
            generate_pages_recursive(item_path, template_path, dest_path, base_path)
            continue
        # if not os.path.isfile(item_path):
        #     generate_pages_recursive(item_path, template_path, dest_dir_path)
        #     continue
        if '.md' in item:
            html_path = dest_path.replace(".md", ".html")
            # print("\n🚨🚨🚨")
            # print(f"dest_path {dest_path}")
            # print(f"html_path {html_path}")
            # print("\n🚨🚨🚨")
            generate_page(item_path, template_path, html_path, base_path)
            continue
