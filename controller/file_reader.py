from mapper import map_to_person_from_string

# Funcion que lee el archivo txt y retorna una lista de personas
def read_file(file_name):
    people = []
    with open(file_name, 'r') as file:
        for line in file:
            people.append(map_to_person_from_string(line))
    return people
