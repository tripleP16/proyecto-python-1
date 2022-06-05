
def select_participant_with_the_lowest_time(participants):
    """
    Selecciona un ganador de la lista de participantes. (La persona con menor tiempo)
    """
    return min(participants, key=lambda p: p.final_time.return_time_format())

