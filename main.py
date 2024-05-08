import display as d
import file_management as fm


def main():
    path = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\circuits\\"
    titles = fm.get_file_titles_in_folder(path)
    circuits = []
    for title in titles:
        file_path = path + title + ".yml"
        yaml_data = fm.open_yaml_file(file_path)
        circuits.append(yaml_data)
    while True:
        find_circuit = input("\nWhat circuit are your searching ?")
        found_circuits, index = d.search_circuit(circuits, find_circuit)
        if found_circuits:
            d.display_circuit(circuits[index])
        else:
            print(f"\nThe circuit {find_circuit} is not in the database.")


# Example usage:
if __name__ == "__main__":
    main()
