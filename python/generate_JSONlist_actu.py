import os
import json
from datetime import datetime

def generate_JSONlist_actu(directory=None, output=None):
    # Obtenir le répertoire du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir les chemins par défaut si aucun n'est spécifié
    directory = directory or os.path.join(script_directory, '../pdf')
    output = output or os.path.join(script_directory, '../json/file_list.json')

    # Initialiser la structure de données pour les fichiers PDF
    pdf_files = {'toujours': []}
    always_dir = os.path.join(directory, 'toujours')

    # Ajouter les fichiers du dossier "toujours"
    if os.path.exists(always_dir):
        pdf_files['toujours'] = [f.replace('.pdf', '') for f in os.listdir(always_dir) if f.endswith('.pdf')]

    # Obtenir le mois actuel
    current_month = datetime.now().strftime('%B').lower()

    # Parcourir tous les dossiers dans le répertoire spécifié
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path) and subdir.lower() == current_month:
            pdf_files[subdir] = [f.replace('.pdf', '') for f in os.listdir(subdir_path) if f.endswith('.pdf')]

    # Écrire la liste des fichiers dans un fichier JSON
    with open(output, 'w') as json_file:
        json.dump(pdf_files, json_file, indent=4)
        
    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_JSONlist_actu()
