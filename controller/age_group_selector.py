def select_age_group(participants, age_group):
    """
    Selecciona a los participantes de un grupo etario en particular y los retorna en una lista nueva
    :param participants: lista de participantes
    :param age_group: grupo etario
    :return: lista de participantes
    """
    if age_group == 0:
        return [participant for participant in participants if participant.age <= 25]
    if age_group == 1:
        return [participant for participant in participants if 25 < participant.age <= 40]
    if age_group == 2:
        return [participant for participant in participants if participant.age > 40]
