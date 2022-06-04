from mapper import map_to_person_from_string


def read_file(file_name):
    people = []
    with open(file_name, 'r') as file:
        for line in file:
            people.append(map_to_person_from_string(line))
    return people


print(read_file('../data/competencia.txt')[0].final_time.return_time_format())
