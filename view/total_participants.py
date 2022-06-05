from controller.file_reader import read_file
from controller.age_group_selector import select_age_group
from controller.gender_selector import gender_selector
from view.table_header import print_table_header


def show_participants(participants):
    """
    Muestra todos los datos de todos los participantes.
    """
    print("\nParticipantes:")

    print_table_header()
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


