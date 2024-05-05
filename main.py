import display as d
import file_management as fm


def main():
    nb_file = fm.count_files_in_folder(r"C:\Users\Antoine Dupont\Desktop\F1 Stats Project\f1db\circuits")
    titles = fm.get_file_titles_in_folder(r"C:\Users\Antoine Dupont\Desktop\F1 Stats Project\f1db\circuits")
    for title in titles:
        file_path = "circuits\\" + title + ".yml"
        yaml_data = fm.open_yaml_file(file_path)
        d.display_circuit(yaml_data)


# Example usage:
if __name__ == "__main__":
    main()
