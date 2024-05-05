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