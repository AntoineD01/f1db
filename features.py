from fuzzywuzzy import fuzz

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
    
    # Look for an exact match
    for i, sdata in enumerate(database):
        if sdata.get('name', '') == data:
            found = True
            index = i
            break

    # Look for closest match
    if found == False:
        closest_match, index = search_closest_match(data, [sdata.get('name', '') for sdata in database])
        if closest_match is not None:
            result = get_valid_input(f"Did you meant {closest_match} ? (1 for yes or 2 for no)", ["1","2"])
            if result == 1:
                found = True
    return found, index

def search_closest_match(user_input, database):
    best_match = None
    best_score = 0
    best_index = -1
    index = -1
    for item in database:
        index += 1
        score = fuzz.ratio(user_input, item)
        if score > best_score:
            best_match = item
            best_score = score
            best_index = index
    return best_match, best_index