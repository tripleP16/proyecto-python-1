from exceptions.invalid_file_format_exception import InvalidFileFormatException
from model.person import Person
from model.final_time import FinalTime


def map_to_person_from_string(data):
    """
    Funcion que mapea una cadena de texto a un objeto de tipo Person
    """
    try:
        data_splitter = data.split(",")
        final_time = FinalTime(int(data_splitter[-3]), int(data_splitter[-2]),
                               int(data_splitter[-1]))  # Se crea el objeto final_time
        person = Person(
            data_splitter[0],
            data_splitter[1],
            data_splitter[2],
            data_splitter[3],
            data_splitter[4],
            data_splitter[5],
            data_splitter[6],
            final_time
        )
        return person
    except Exception as e:
        raise InvalidFileFormatException()
