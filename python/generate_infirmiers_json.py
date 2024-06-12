import os
import json

def generate_infirmiers_json(input_file=None, output_file=None):
    # Obtenir le répertoire du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir les chemins par défaut si aucun n'est spécifié
    input_file = input_file or os.path.join(script_directory, '../infirmiers/noms.txt')
    output_file = output_file or os.path.join(script_directory, '../json/infirmiers_content.json')

    infirmiers = []

    # Vérifier si le fichier d'entrée existe
    if not os.path.exists(input_file):
        print(f"Erreur : le fichier d'entrée {input_file} n'existe pas.")
        return
    
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
    
    print(f"Les données ont été écrites avec succès dans {output_file}")

if __name__ == "__main__":
    generate_infirmiers_json()
