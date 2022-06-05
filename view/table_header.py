# Funcion que imprime el encabezado de la tabla
def print_table_header(first_column=None):
    if first_column is not None:
        print(
            ("|{:13}|{:13}|{:15}|{:16}|{:13}|{:13}|{:13}|{:13}|{:13}|".format(first_column, "Cedula", "Primer Apellido",
                                                                              "Segundo Apellido",
                                                                              "Nombre", "Inicial ", "Genero", "Edad",
                                                                              "Tiempo final")))
    else:
        print(
            ("|{:13}|{:15}|{:16}|{:13}|{:13}|{:13}|{:13}|{:13}|".format("Cedula", "Primer Apellido",
                                                                        "Segundo Apellido",
                                                                        "Nombre", "Inicial ", "Genero", "Edad",
                                                                        "Tiempo final")))
