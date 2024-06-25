import os
import json
import shutil

def update_professions():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    ajoutprofession_path = os.path.join(base_path, 'ajoutprofession')
    json_path = os.path.join(base_path, 'json', 'professions.json')
    modele_path = os.path.join(ajoutprofession_path, 'modele.html')

    # List all directories in ajoutprofession except 'modele.html'
    professions = []
    for item in os.listdir(ajoutprofession_path):
        item_path = os.path.join(ajoutprofession_path, item)
        if os.path.isdir(item_path):
            professions.append(item)
            # Copy modele.html to the new profession folder if it doesn't already exist
            dest_path = os.path.join(item_path, 'index.html')
            if not os.path.exists(dest_path):
                shutil.copy(modele_path, dest_path)

    # Save the list of professions to professions.json
    with open(json_path, 'w') as f:
        json.dump(professions, f, indent=4)

    print(f'Updated professions.json with {len(professions)} professions.')

if __name__ == '__main__':
    update_professions()
