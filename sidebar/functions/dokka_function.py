import os
import json
from sidebar.functions.files_function import *

def sidebar_command(path, root_name, root_position, output_path, auto_generated, multi_module, filter_file):
    """This command traverses the dokka directory and
    look for .md files to map the hierarchy of files
    """
    global base_path
    base_path = path

    if auto_generated == True and multi_module == False:
        create_side_bar_category_files(path, root_name, root_position)
        print("Category files created")
    elif auto_generated == True and multi_module == True:
        create_multi_module_side_bar_category_files(path, root_name, filter_file, root_position)
        print("Category files created")
    else:
        create_side_bar_file(path, root_name, output_path)
        print("Sidebar file created at: " + path)

def create_multi_module_side_bar_category_files(path, label, filter_file, root_position):
    module_list = []

    with open(filter_file) as filter_f:
        module_list = json.load(filter_f)

    create_category_file(path, label, root_position)

    for module in module_list:
        file_path = parse_path_from_input(path, module)
        create_side_bar_category_files(file_path, module)

def create_side_bar_category_files(path, label):
    create_category_file(path, label)

    folders_path, _ = folders_and_items(path)
    folders_path.sort()


    for folder_path in folders_path:
        folder_name = os.path.basename(folder_path)
        create_side_bar_category_files(folder_path, folder_name)

def create_side_bar_file(path, root_name, output_file):
    directory_map = directory_tree_to_map(path, root_name)
    sidebar = sidebar_map(directory_map)
    json_dump = json.dumps(sidebar, indent=2, sort_keys=False)

    output_file = parse_path_from_input(output_path, "/sidebars.js")

    with open(output_file, "w") as sidebar_file:
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

def create_category_file(path, label, position=None):
    info = {"label": label}

    if position != None:
        info["position"] = position

    info_json = json.dumps(info, indent=2, sort_keys=False)

    file_path = parse_path_from_input(path, "_category_.json")

    with open(file_path, "w") as category_file:
        category_file.write(info_json)
        category_file.write('\n')
