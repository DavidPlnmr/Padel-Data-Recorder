def create_rally(eq1, eq2):
    return {'t0': None, 'events': [], 'eq1': eq1, 'eq2': eq2, 'service': eq1}

def save_rally(rally, filepath):
    import json
    with open(filepath, "a") as f:
        json.dump(rally, f)
        f.write('\n')

def remove_last_event(rally):
    if rally['events']:
        rally['events'].pop()