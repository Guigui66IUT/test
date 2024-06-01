import os
import json

def generate_infirmiers_json(input_file='infirmiers/noms.txt', output_file='infirmiers_content.json'):
    infirmiers = []
    
    # Lire les noms depuis le fichier texte
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Ajouter chaque nom au dictionnaire
    for line in lines:
        name = line.strip()
        if name:  # S'assurer qu'il n'y a pas de lignes vides
            infirmiers.append({'name': name})
    
    # Écrire les données dans le fichier JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(infirmiers, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    generate_infirmiers_json()
