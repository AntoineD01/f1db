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
    path = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\grands-prix\\"
    grand_prix = fm.store_data(path)
    seasons_folder = r"C:\\Users\Antoine Dupont\Desktop\\F1 Stats Project\\f1db\src\data\\seasons\\"
    years = range(1950, 2025)
    driver_standings = {}
    constructors_standings = {}
    for year in years:
        driver_path = seasons_folder + str(year) + "\driver-standings.yml"
        driver_standings[year] = fm.store_file(driver_path)
        if year >=1958:
            construct_path = seasons_folder + str(year) + "\constructor-standings.yml"
            constructors_standings[year] = fm.store_file(construct_path)
    print(driver_standings[1950])
    print(constructors_standings[1958])

    while True:
        to_do = f.get_valid_input("\n\nWhat do you want to search (1 circuit, 2 constructor, 3 drivers, 4 grand-prix, 5 for the standings,0 to stop) ?\n", ["1","2","3","4","5","0"])
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
        elif to_do==4:
            find_gp = input("\nWhat GP are your searching ?\n")
            found, index = f.search(grand_prix, find_gp)
            if found:
                d.display_gp(grand_prix[index])
            else:
                print(f"\nThe grand prix {find_gp} is not in the database.")
        elif to_do==5:
            year = 0
            while(year<1950 or year>2024):
                year = int(input("\nWhat year do you want to see (1950-2024) ?\n"))
            c_or_d = f.get_valid_input("Do you want to see the driver standings (1) or the constructor-standings (2)?",["1","2"])
            if year < 1958 and c_or_d == 2:
                print("\nThere is no constructor standings before 1958.")
            elif c_or_d == 1:
                d.display_standings(driver_standings[year])
            else:
                d.display_standings(constructors_standings[year])
        elif to_do==0:
            break


# Example usage:
if __name__ == "__main__":
    main()
