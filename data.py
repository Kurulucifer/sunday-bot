import os
import json

def grab_parent(file):
    path = os.getcwd()
    parent = os.path.dirname(path)
    with open(parent + f'\{file}.json', 'r') as f:
        return json.load(f)
