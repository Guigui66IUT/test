import os
import json
from datetime import datetime

def generate_JSONlist_actu(directory=None, output=None):
    # Mappage des noms de mois en anglais vers le français
    months_translation = {
        'january': 'janvier',
        'february': 'fevrier',
        'march': 'mars',
        'april': 'avril',
        'may': 'mai',
        'june': 'juin',
        'july': 'juillet',
        'august': 'aout',
        'september': 'septembre',
        'october': 'octobre',
        'november': 'novembre',
        'december': 'decembre'
    }

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
        pdf_files['toujours'] = always_files
    else:
        print(f"Le dossier 'toujours' n'existe pas dans {directory}")

    # Obtenir le mois actuel en anglais et le traduire en français
    current_month_english = datetime.now().strftime('%B').lower()
    current_month = months_translation.get(current_month_english, current_month_english)
    print(f"Mois actuel: {current_month}")

    # Parcourir tous les dossiers dans le répertoire spécifié
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path) and subdir.lower() == current_month:
            month_files = [f.replace('.pdf', '') for f in os.listdir(subdir_path) if f.endswith('.pdf')]
            pdf_files[subdir] = [file for file in month_files if file not in always_files]
            print(f"Fichiers dans '{subdir}': {pdf_files[subdir]}")
        elif subdir.lower() != 'toujours' and os.path.isdir(subdir_path):
            print(f"Ignoré le dossier: {subdir}")

    # Écrire la liste des fichiers dans un fichier JSON
    with open(output, 'w', encoding='utf-8') as json_file:
        json.dump(pdf_files, json_file, indent=4, ensure_ascii=False)

    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_JSONlist_actu()
