from file_reader import read_file
from age_group_selector import select_age_group
from gender_selector import gender_selector


def show_participants(participants):
    """
    Muestra todos los datos de todos los participantes.
    """
    print("\nParticipantes:")

    print(("|{:13}|{:15}|{:16}|{:13}|{:13}|{:13}|{:13}|{:13}|".format("Cedula", "Primer Apellido", "Segundo Apellido",
                                                                      "Nombre", "Inicial ", "Genero", "Edad",
                                                                      "Tiempo final")))
    for participant in participants:
        print(str(participant))


def total_participants(participants):
    """
    Muestra la totalidad de los participantes.
    """
    print("\nTotal de participantes: ", len(participants))


def total_participants_by_age_group(participants):
    """
    Muestra la totalidad de los participantes por grupo de edad.
    """
    print("\nTotal de participantes por grupo de edad: ")
    print("|{:13}|{:13}|".format("Grupo de edad", "Total"))
    juniors = select_age_group(participants, 0)
    seniors = select_age_group(participants, 1)
    masters = select_age_group(participants, 2)
    print("|{:13}|{:13}|".format("Juniors", len(juniors)))
    print("|{:13}|{:13}|".format("Seniors", len(seniors)))
    print("|{:13}|{:13}|".format("Masters", len(masters)))


def total_participants_by_gender(participants):
    """
    Muestra el total de participantes por genero
    :param participants:
    :return:
    """
    men = gender_selector(participants, "M")
    women = gender_selector(participants, "F")
    print("\nCantidad de participantes por genero ")
    print("{:13} {:13}".format("Mujeres: ", len(women)))
    print("{:13} {:13}".format("Hombres: ", len(men)))


show_participants(read_file("../data/competencia.txt"))
total_participants(read_file("../data/competencia.txt"))
total_participants_by_age_group(read_file("../data/competencia.txt"))
total_participants_by_gender(read_file("../data/competencia.txt"))