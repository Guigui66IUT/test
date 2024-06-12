import os
import json

def generate_TraitementKine_json(directory='traitementkine', output='traitementkine_content.json'):
    medecins = []

    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            treatment_name = filename.replace('.jpg', '').replace('_', ' ').upper()

            medecin = {
                'name': treatment_name,
                'image': os.path.join(directory, filename)
            }
            medecins.append(medecin)

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(medecins, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    generate_TraitementKine_json()
