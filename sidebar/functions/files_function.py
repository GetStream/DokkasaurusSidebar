def remove_path_from_file(path):
    return path.rsplit("/", 1)[0]

def remove_extension(path):
    return path.rsplit(".", 1)[0]

def is_markdown(file_path):
    return file_path.endswith(".md")

def is_index_file(file_path):
    return file_path.endswith("index.md")

def parse_path_from_input(input_path, file):
    if input_path.endswith("/"):
        return input_path + file
    else:
        return input_path + "/" + file
