import display as d
import file_management as fm


def main():
    path = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\circuits\\"
    circuits = fm.store_data(path)
    path = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\constructors\\"
    constructors = fm.store_data(path)
    
    while True:
        to_do = int(input("\n\nWhat do you want to search (1 for circuit, 2 for constructor) ?\n"))
        if to_do==1:
            find_circuit = input("\nWhat circuit are your searching ?\n")
            found, index = d.search(circuits, find_circuit)
            if found:
                d.display_circuit(circuits[index])
            else:
                print(f"\nThe circuit {find_circuit} is not in the database.")
        elif to_do==2:
            find_construc = input("\nWhat constructor are your searching ?\n")
            found, index = d.search(constructors, find_construc)
            if found:
                d.display_constructors(constructors[index])
            else:
                print(f"\nThe constructor {find_construc} is not in the database.")


# Example usage:
if __name__ == "__main__":
    main()
