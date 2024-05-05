import yaml

def open_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except yaml.YAMLError as e:
        print(f"Error while parsing YAML file: {e}")

# Example usage:
if __name__ == "__main__":
    file_path = "adelaide.yml"
    yaml_data = open_yaml_file(file_path)
    if yaml_data:
        print("YAML file contents:")
        print(yaml_data)