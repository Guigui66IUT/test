import os
import json

def update_professions():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    ajoutprofession_path = os.path.join(base_path, 'ajoutprofession')
    json_path = os.path.join(base_path, 'json', 'professions.json')

    # List all directories in ajoutprofession except 'modele.html'
    professions = []
    for item in os.listdir(ajoutprofession_path):
        item_path = os.path.join(ajoutprofession_path, item)
        if os.path.isdir(item_path) and item != 'modele.html':
            professions.append(item)

    # Save the list of professions to professions.json
    with open(json_path, 'w') as f:
        json.dump(professions, f, indent=4)


if __name__ == '__main__':
    update_professions()
