def gender_selector(participants, gender):
    return [participant for participant in participants if participant.gender.lower() == gender.lower()]