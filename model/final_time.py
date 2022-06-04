from datetime import time
class FinalTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def return_time_format(self):
        time_format = time(self.hours, self.minutes, self.seconds)
        return time_format
