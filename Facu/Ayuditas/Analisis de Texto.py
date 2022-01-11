def es_vocal(car):
    if car in 'aeiouAEIOU':
        return True
    else:
        return False


def es_digito(car):
    if car in '1234567890':
        return True
    else:
        return False


def es_terminador(car):
    if car in ' .':
        return True
    else:
        return False


def es_consonante(car):
    if car in 'BbCcDdFfGgHhJjKkLlMmÑñPpQqRrSsTtVvWwXxYyzZ':
        return True
    else:
        return False
    
