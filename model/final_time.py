from datetime import time
# Clase FinalTime que representa el tiempo transcurrido en la competencia

class FinalTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # Funcion que formatea el tiempo transcurrido en la competencia a un objeto de tipo time
    def return_time_format(self):
        time_format = time(self.hours, self.minutes, self.seconds)
        return time_format
