# Clase que representa un competidor

class Person:
    def __init__(self, id, first_last_name, second_last_name, name, middle_initial, gender, age, final_time):
        self.id = id
        self.first_last_name = first_last_name
        self.second_last_name = second_last_name
        self.name = name
        self.middle_initial = middle_initial
        self.gender = gender
        self.age = int(age)
        self.final_time = final_time

    def __str__(self):
        return "|{:13}|{:15}|{:16}|{:13}|{:13}|{:13}|{:13}|{:13}|"\
            .format(self.id, self.first_last_name, self.second_last_name,
                    self.name, self.middle_initial, self.gender,
                    self.age, str(self.final_time.return_time_format()))
