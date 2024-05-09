from geopy.geocoders import Nominatim

def get_city(latitude, longitude):
    geolocator = Nominatim(user_agent="city_locator")
    location = geolocator.reverse((latitude, longitude))
    address = location.raw['address']
    city = address.get('city', '')
    if not city:
        city = address.get('town', '')
    if not city:
        city = address.get('village', '')
    return city

def display_circuit(data):
    print('\n\nCIRCUIT\nName :', data['name'])
    if data['previousNames'] != None:
        print('Also known as', data['previousNames'])
    print("Country :",data['countryId'].capitalize())
    city = get_city(data['latitude'], data['longitude'])
    print("City :", city)

def display_constructors(data):
    print('\n\nCONSTRUCTOR\nName :', data['name'])
    
    previous_constructors = data.get('previousNextConstructors', [])
    if previous_constructors:
        print('Name history:')
        for constructor in previous_constructors:
            constructor_id = constructor.get('constructorId', '')
            year_from = constructor.get('yearFrom', '')
            year_to = constructor.get('yearTo', '')
            if year_to is None:
                year_to_display = "Now"
            else:
                year_to_display = year_to
            print(f"  - Constructor Name: {constructor_id.capitalize()}, Years: {year_from} to {year_to_display}")

def display_driver(data):
    print('\n\nDRIVER\nName :', data['fullName'])
    print("Gender :",data["gender"])
    print(f"Birth: {data['dateOfBirth']} in {data['placeOfBirth']}, {data['countryOfBirthCountryId'].capitalize()}")
    if data["dateOfDeath"]!= None:
        print("Death :", data["dateOfBirth"])

def display_gp(data):
    print('\n\nGRAND PRIX\nName :', data['fullName'])
    print("Country :",data["countryId"].capitalize())
    
def display_standings(data):
    print("{:<10}{:<25}{:<10}".format("Position", "Driver ID", "Points"))
    print("-" * 50)
    for entry in data:
        position = entry['position']
        driver_id = entry['driverId']
        points = entry['points']
        print("{:<10}{:<25}{:<10}".format(position, driver_id.capitalize(), points))