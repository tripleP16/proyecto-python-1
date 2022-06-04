from model.person import Person
from model.final_time import FinalTime

def map_to_person_from_string(data):

    """
    Maps a string to a person object.
    """
    data_splitter = data.split(",")
    final_time = FinalTime(int(data_splitter[-3]), int(data_splitter[-2]), int(data_splitter[-1]))
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


