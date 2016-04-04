def clean_json(data):
    if 'ip' in data and 'error' in data and len(data) == 2:
        return True
    return False
