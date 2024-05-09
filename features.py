
def get_valid_input(question, accepted_values):
    while True:
        user_input = input(question)
        if user_input in accepted_values:
            return int(user_input)
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(accepted_values)}.")

def two_part_input(data):
    words = data.split()
    if len(words) == 2:
        capitalized_second_word = words[1].capitalize()
        output_string = words[0] + " " + capitalized_second_word
        return True, output_string
    else:
        return False, None

def search(database, data):
    found = False
    index = None  
    for i, sdata in enumerate(database):
        if sdata.get('name', '') == data:
            found = True
            index = i
            break
    #Look with a capital letter at first
    data = data.capitalize()
    for i, sdata in enumerate(database):
        if sdata.get('name', '') == data:
            found = True
            index = i
            break
    #Look with full caps
    data = data.upper() 
    for i, sdata in enumerate(database):
        if sdata.get('name', '') == data:
            found = True
            index = i
            break
    #Look with caps on each part of the input
    valid, capdata = two_part_input(data)
    if valid:
        for i, sdata in enumerate(database):
            if sdata.get('name', '') == capdata:
                found = True
                index = i
                break
    return found, index