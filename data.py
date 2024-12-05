import os
import json

def grab_json(file):
    with open(f'{file}.json', 'r') as f:
        return json.load(f)
