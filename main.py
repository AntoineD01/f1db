import display as d
import file_management as fm


def main():
    file_path = r"circuits\adelaide.yml"
    yaml_data = fm.open_yaml_file(file_path)
    d.display_circuit(yaml_data)
    nb_file = fm.count_files_in_folder(r"C:\Users\Antoine Dupont\Desktop\F1 Stats Project\f1db\circuits")
    #for i in range(nb_file):

# Example usage:
if __name__ == "__main__":
    main()
