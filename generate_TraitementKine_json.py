import os
import json
import re

def generate_TraitementKine_json(directory='traitementkine', output='traitementkine_content.json'):
    medecins = []

    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            # Récupérer le nom du traitement et le numéro
            match = re.match(r'^(.*)_(\d+)\.jpg$', filename)
            if match:
                treatment_name = match.group(1).replace('_', ' ').upper()
                order = int(match.group(2))

                medecin = {
                    'name': treatment_name,
                    'image': os.path.join(directory, filename),
                    'order': order
                }
                medecins.append(medecin)

    # Trier les médecins par ordre
    medecins = sorted(medecins, key=lambda x: x['order'])

    # Écrire les données dans un fichier JSON
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(medecins, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    generate_TraitementKine_json()
