import os
import json
import locale
from datetime import datetime

def generate_JSONlist_actu(directory=None, output=None):
    # Définir la locale en français
    locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')

    # Obtenir le répertoire du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir les chemins par défaut si aucun n'est spécifié
    directory = directory or os.path.join(script_directory, '../pdf')
    output = output or os.path.join(script_directory, '../json/file_list.json')

    # Initialiser la structure de données pour les fichiers PDF
    pdf_files = {}
    always_files = []
    always_dir = os.path.join(directory, 'toujours')

    # Ajouter les fichiers du dossier "toujours"
    if os.path.exists(always_dir):
        always_files = [f.replace('.pdf', '') for f in os.listdir(always_dir) if f.endswith('.pdf')]
        print(f"Fichiers dans 'toujours': {always_files}")
    else:
        print(f"Le dossier 'toujours' n'existe pas dans {directory}")

    # Obtenir le mois actuel en français
    current_month = datetime.now().strftime('%B').lower()
    print(f"Mois actuel: {current_month}")

    # Parcourir tous les dossiers dans le répertoire spécifié
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path) and subdir.lower() == current_month:
            pdf_files[subdir] = always_files + [f.replace('.pdf', '') for f in os.listdir(subdir_path) if f.endswith('.pdf')]
            print(f"Fichiers dans '{subdir}': {pdf_files[subdir]}")
        elif subdir.lower() != 'toujours' and os.path.isdir(subdir_path):
            print(f"Ignoré le dossier: {subdir}")

    # Si aucun fichier du mois actuel n'a été trouvé, inclure uniquement les fichiers 'toujours'
    if not pdf_files:
        pdf_files['toujours'] = always_files
        print(f"Utilisation de fichiers 'toujours' uniquement: {always_files}")

    # Écrire la liste des fichiers dans un fichier JSON
    with open(output, 'w') as json_file:
        json.dump(pdf_files, json_file, indent=4)
        
    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_JSONlist_actu()
