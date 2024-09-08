import os
import json
import re

def generate_TraitementPodo_json(directory=None, output=None):
    # Obtenir le répertoire du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir les chemins par défaut si aucun n'est spécifié
    directory = directory or os.path.join(script_directory, '../podologues/traitement/')  # Modifié pour 'traitementpodo'
    output = output or os.path.join(script_directory, '../json/traitementpodo_content.json')  # Modifié pour 'traitementpodo'

    traitements = []

    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            # Récupérer le nom du traitement et le numéro
            match = re.match(r'^(.*)_(\d+)\.jpg$', filename)
            if match:
                treatment_name = match.group(1).replace('_', ' ').upper()
                order = int(match.group(2))

                traitement = {
                    'name': treatment_name,
                    'image': filename,  # Récupérer uniquement le nom de l'image
                    'order': order
                }
                traitements.append(traitement)

    # Trier les traitements par ordre
    traitements = sorted(traitements, key=lambda x: x['order'])

    # Créer le répertoire JSON s'il n'existe pas
    output_dir = os.path.dirname(output)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Écrire les données dans un fichier JSON
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(traitements, f, indent=4, ensure_ascii=False)
    
    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_TraitementPodo_json()
