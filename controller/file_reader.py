from controller.mapper import map_to_person_from_string
from exceptions.invalid_file_format_exception import InvalidFileFormatException


def read_file(file_name):
    people = []
    with open(file_name, 'r') as file:
        for line in file:
            try:
                people.append(map_to_person_from_string(line))
            except Exception as e:
                raise InvalidFileFormatException()
    return people
