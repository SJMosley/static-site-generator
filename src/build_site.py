import os
import shutil

def testing():
    print(os.listdir('..'))


def delete_folder(path):
    print(f"deleting {path}")
    shutil.rmtree(path, True)

def copy_tree(from_dir, to_dir):

    # os.listdir to get items
    dir_items = os.listdir(from_dir)

    for dir_item in dir_items:
        curr_dir_item = os.path.join(from_dir, dir_item)
        if not os.path.isfile(curr_dir_item):
            new_dir_path = os.path.join(to_dir, dir_item)
            os.mkdir(new_dir_path)
            #recursive call on directories (dir is made on next call)
            copy_tree(curr_dir_item, os.path.join(to_dir, dir_item))
            continue
        print(f"from {from_dir} to {to_dir}")
        new_path = os.path.join(to_dir, dir_item)
        print(f"Copying to new path {new_path}")
        shutil.copy(curr_dir_item, new_path)

def publish_content(from_dir, dest_dir):
    delete_dest_dir_before_publish(dest_dir)
    #no to_dir. Yeet!
    if not os.path.exists(from_dir):
        print("path does not exist")
        return

    print(f"public path exists? {os.path.exists(dest_dir)}")
    print(f"static path exists? {os.path.exists(from_dir)}")

    #copy from static to directory
    copy_tree(from_dir, dest_dir)

def delete_dest_dir_before_publish(dest_dir):
    #delete first
    if os.path.exists(dest_dir):
        delete_folder(dest_dir)

    #remake it!
    if not os.path.exists(dest_dir):
        print(f"creating {dest_dir[1:]}")
        os.mkdir(dest_dir)


# testing()
# publish_content()
