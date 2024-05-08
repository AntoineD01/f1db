import display as d
import file_management as fm


def main():
    path = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\circuits\\"
    circuits = fm.store_circuit(path)
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
