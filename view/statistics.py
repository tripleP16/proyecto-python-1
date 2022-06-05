import datetime

from controller.age_group_selector import select_age_group
from controller.average_time import average_time
from controller.gender_selector import gender_selector


def show_histogram(participants):
    """
    Funcion que muestra un histograma por cada una de los grupos etarios
    """
    juniors = select_age_group(participants, 0)
    seniors = select_age_group(participants, 1)
    masters = select_age_group(participants, 2)
    print("Histograma de participantes por grupo etario")
    print_histogram(len(juniors), "Juniors")
    print_histogram(len(seniors), "Seniors")
    print_histogram(len(masters), "Masters")


# Funcion que devuelve los * para el histograma
def get_characters(number):
    aux = ""
    for i in range(number):
        aux += "*"
    return aux


# Funcion que imprime el histograma
def print_histogram(length, age_group):
    print("{:13}|{:13}".format(age_group + "(" + str(length) + ")", get_characters(length)))


def print_average_time_by_age_and_gender(participants, gender=None):
    if gender is not None:
        participants = gender_selector(participants, gender)
        if gender.upper() == "M":
            print("Genero Masculino")
        if gender.upper() == "F":
            print("Genero Femenino")
    juniors = select_age_group(participants, 0)
    seniors = select_age_group(participants, 1)
    masters = select_age_group(participants, 2)
    print("Tiempo promedio de registro por grupo etario")
    print("Juniors: " + str(datetime.timedelta(seconds=average_time(juniors))))
    print("Seniors: " + str(datetime.timedelta(seconds=average_time(seniors))))
    print("Masters: " + str(datetime.timedelta(seconds=average_time(masters))))


