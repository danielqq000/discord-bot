import json
import os

DATA_FILE = 'data/player_data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def create_character(user_id, name):
    data = load_data()
    if str(user_id) in data:
        return False
    data[str(user_id)] = {
        "name": name,
        "level": 1,
        "experience": 0,
        "health": 100,
        "mana": 50,
        "attack": 10,
        "defense": 5
    }
    save_data(data)
    return True

def get_character(user_id):
    data = load_data()
    return data.get(str(user_id), None)
