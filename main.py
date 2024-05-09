import display as d
import file_management as fm
import features as f


def main():
    path = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\circuits\\"
    circuits = fm.store_data(path)
    path = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\constructors\\"
    constructors = fm.store_data(path)
    path = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\drivers\\"
    drivers = fm.store_data(path)
    while True:
        to_do = f.get_valid_input("\n\nWhat do you want to search (1 for circuit, 2 for constructor, 3 for drivers, 0 to stop) ?\n", ["1","2","3","0"])
        if to_do==1:
            find_circuit = input("\nWhat circuit are your searching ?\n")
            found, index = f.search(circuits, find_circuit)
            if found:
                d.display_circuit(circuits[index])
            else:
                print(f"\nThe circuit {find_circuit} is not in the database.")
        elif to_do==2:
            find_construc = input("\nWhat constructor are your searching ?\n")
            found, index = f.search(constructors, find_construc)
            if found:
                d.display_constructors(constructors[index])
            else:
                print(f"\nThe constructor {find_construc} is not in the database.")
        elif to_do==3:
            find_driver = input("\nWhich driver are your searching ?\n")
            found, index = f.search(drivers, find_driver)
            if found:
                d.display_driver(drivers[index])
            else:
                print(f"\nThe driver {find_driver} is not in the database.")
        elif to_do==0:
            break


# Example usage:
if __name__ == "__main__":
    main()
