from controller.age_group_selector import select_age_group
from controller.select_winner import select_participant_with_the_lowest_time
from view.table_header import print_table_header
from controller.gender_selector import gender_selector


def winners_by_age_group(participants, gender=None):
    """
    Esta funcion imprime los ganadores por grupo de edad y de acuerdo al genero a traves de un parametro opcional
    """
    if gender is not None:
        participants = gender_selector(participants, gender)
        if gender.upper() == "M":
            print("Genero Masculino")
        if gender.upper() == "F":
            print("Genero Femenino")
    juniors = select_age_group(participants, 0)
    seniors = select_age_group(participants, 1)
    masters = select_age_group(participants, 2)
    junior_winner = select_participant_with_the_lowest_time(juniors)
    seniors_winner = select_participant_with_the_lowest_time(seniors)
    masters_winner = select_participant_with_the_lowest_time(masters)
    print("Los ganadores por grupo de edad son:")
    print_table_header("Categoria")
    print("|{:13}{:13}".format("Junior", str(junior_winner)))
    print("|{:13}{:13}".format("Seniors", str(seniors_winner)))
    print("|{:13}{:13}".format("Masters", str(masters_winner)))


def winners_by_gender(participants):
    """
    Esta funcion imprime los ganadores de acuerdo al genero
    """
    men = gender_selector(participants, "M")
    women = gender_selector(participants, "F")
    mens_winner = select_participant_with_the_lowest_time(men)
    women_winner = select_participant_with_the_lowest_time(women)
    print("Los Ganadores por sexo son: ")
    print_table_header("Genero")
    print("|{:13}{:13}".format("Mujeres", str(women_winner)))
    print("|{:13}{:13}".format("Hombres", str(mens_winner)))


def general_winner(participants):
    """
        Funcion que imprime el ganador general
    """
    winner = select_participant_with_the_lowest_time(participants)
    print("El ganador general es: ")
    print_table_header()
    print(str(winner))


