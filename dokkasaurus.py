import click
import os
import json

base_path = "./"

@click.command()
@click.argument('path')
@click.argument('root_name')
def cli(path, root_name):
    """This command traverses the dokka directory and
    look for .md files to map the hierarchy of files
    """
    global base_path
    base_path = path

    directory_map = directory_tree_to_map(path, root_name)
    sidebar = sidebar_map(directory_map)
    json_dump = json.dumps(sidebar, indent=2, sort_keys=False)

    with open("sidebars.js", "w") as sidebar_file:
        sidebar_file.write("module.exports = ")
        sidebar_file.write(json_dump)

def sidebar_map(content_map):
    docs_list = list()
    docs_list.append(content_map)
    return {"docs": docs_list}

def folders_and_items(path):
    directory_files = os.listdir(path)
    directory_paths = list(map(lambda x: os.path.join(path, x), directory_files))
    folders_path = list(filter(lambda x: os.path.isdir(x), directory_paths))
    items_path = [item for item in directory_paths if item not in folders_path]

    folders = list(map(os.path.basename, folders_path))
    items = list(map(os.path.basename, items_path))

    return folders_path, items_path

def get_docussauros_id(file_path):
    path_without_base = file_path.replace(base_path, "", 1)

    if path_without_base.startswith("/"):
        path_without_base = path_without_base[1:]

    return remove_extension(path_without_base)

def remove_extension(path):
    return path.rsplit(".", 1)[0]

def directory_tree_to_map(path, label):
    directory_map = {}
    directory_map['label'] = label
    directory_map['type'] = "category"

    folders_path, items_path = folders_and_items(path)

    cleaned_items = list(filter(is_markdown, items_path))
    items = list(map(get_docussauros_id, cleaned_items))
    items.sort()

    for folder_path in folders_path:
        folder_name = os.path.basename(folder_path)
        items.append(directory_tree_to_map(folder_path, folder_name))

    directory_map['items'] = organize_items(items, label)

    return directory_map

def organize_items(items, label):
    for item in items:
        if str(item).endswith("index"):
            items.remove(item)
            items.insert(0, item)
        elif str(item).endswith(label):
            if str(items[0]).endswith("index"):
                items.remove(item)
                items.insert(1, item)
            else:
                items.remove(item)
                items.insert(0, item)
    return items

def is_markdown(file_path):
    return file_path.endswith(".md")

def is_index_file(file_path):
    return file_path.endswith("index.md")
