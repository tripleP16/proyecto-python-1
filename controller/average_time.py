

def average_time(participants):
    """
    Funcion que calcula el tiempo promedio de cada participante
    """
    total_time = 0
    for participant in participants:
        time = participant.final_time.return_time_format()
        seconds = (time.hour * 3600) + (time.minute * 60) + time.second
        total_time += seconds
    return total_time / len(participants)


