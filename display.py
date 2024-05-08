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
    print("\n\nCIRCUIT")
    print('Name :', data['name'])
    if data['previousNames'] != None:
        print('Also known as', data['previousNames'])
    print("Country :",data['countryId'])
    city = get_city(data['latitude'], data['longitude'])
    print("City :", city)

def search_circuit(circuits, circuit_name):
    found_circuit = False
    index = None  
    for i, circuit in enumerate(circuits):
        if circuit.get('name', '') == circuit_name:
            found_circuit = True
            index = i
            break
    #Look with a capital letter at first
    circuit_name = circuit_name.capitalize()
    for i, circuit in enumerate(circuits):
        if circuit.get('name', '') == circuit_name:
            found_circuit = True
            index = i
            break
    #Look with full caps
    circuit_name = circuit_name.upper() 
    for i, circuit in enumerate(circuits):
        if circuit.get('name', '') == circuit_name:
            found_circuit = True
            index = i
            break
    
    return found_circuit, index