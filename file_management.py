import yaml
import os

def open_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except yaml.YAMLError as e:
        print(f"Error while parsing YAML file: {e}")

def get_file_titles_in_folder(folder_path):
    file_titles = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            title, _ = os.path.splitext(file_name)
            file_titles.append(title)
    return file_titles

def count_files_in_folder(folder_path):
    count = 0
    for _, _, files in os.walk(folder_path):
        count += len(files)
    return count