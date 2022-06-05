from controller.file_reader import read_file
from controller.validator import validate_file_extension
from exceptions.invalid_extension_exception import InvalidFileExtensionError
from exceptions.invalid_file_format_exception import InvalidFileFormatException
from view.total_participants import show_participants, total_participants, total_participants_by_age_group, total_participants_by_gender
from view.winners_view import winners_by_age_group, winners_by_gender, general_winner
from view.statistics import show_histogram, print_average_time_by_age_and_gender


def clear():
    print("\n" * 100)


def actions_menu(participants):
    check = True
    clear()
    while check:
        print("Bienvenido al menu de acciones")
        print("1. Mostrar todos los participantes")
        print("2. Mostrar la cantidad total de participantes")
        print("3. Mostrar la cantidad de participantes por grupo etario")
        print("4. Mostrar la cantidad de participantes por sexo")
        print("5. Mostrar los ganadores de cada grupo etario")
        print("6. Mostrar los ganadores de cada sexo")
        print("7. Mostrar los ganadores de cada grupo etario y sexo")
        print("8. Mostrar al ganador general")
        print("9. Mostrar histograma de participantes por grupo etario")
        print("10. Mostrar promedio de tiempo por grupo etario y sexo")
        print("11. Salir")
        option = input("Ingrese una opcion: ")
        if option == "1":
            show_participants(participants)
        if option == "2":
            total_participants(participants)
        if option == "3":
            total_participants_by_age_group(participants)
        if option == "4":
            total_participants_by_gender(participants)
        if option == "5":
            winners_by_age_group(participants)
        if option == "6":
            winners_by_gender(participants)
        if option == "7":
            winners_by_age_group(participants, "F")
            winners_by_age_group(participants, "M")
        if option == "8":
            general_winner(participants)
        if option == "9":
            show_histogram(participants)
        if option == "10":
            print_average_time_by_age_and_gender(participants, "F")
            print_average_time_by_age_and_gender(participants, "M")
        if option == "11":
            check = False
        else:
            print("Opcion incorrecta")
            aux = input("Presione enter para continuar")
        aux = input("Presione enter para continuar")
        clear()


def main_menu():
    check = True
    while check:
        print("Bienvenido al menu de competencias")
        print("1. Leer archivo")
        print("2. Salir")
        option = input("Ingrese una opcion: ")
        if option == "1":
            file = input("Ingrese el nombre del archivo con la extension .txt previamente cargado en el directorio "
                         "data: ")
            try:
                validate_file_extension(file)
                file_to_pass = "../data/" + file
                participants = read_file(file_to_pass)
                actions_menu(participants)
            except FileNotFoundError:
                print("El archivo no existe en el directorio data")
            except ValueError:
                print("El archivo no es valido")
            except InvalidFileExtensionError:
                print("Tipo de archivo incorrecto")
            except InvalidFileFormatException:
                print("Cantidad de columnas incorrecta")
        if option == "2":
            check = False
        else:
            print("Opcion incorrecta")
            aux = input("Presione enter para continuar")


main_menu()
