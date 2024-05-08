
def get_valid_input(question, accepted_values):
    while True:
        user_input = input(question)
        if user_input in accepted_values:
            return int(user_input)
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(accepted_values)}.")


def search(circuits, circuit_name):
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