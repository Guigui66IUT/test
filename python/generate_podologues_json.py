import os
import json
import re

def extract_number_from_folder(folder_name):
    """Extraire le numéro du nom du dossier, sinon retourner un grand numéro."""
    match = re.search(r'\d+', folder_name)
    return int(match.group()) if match else float('inf')

def generate_podologues_json(directory=None, output=None):
    # Obtenir le répertoire du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir les chemins par défaut si aucun n'est spécifié
    directory = directory or os.path.join(script_directory, '../podologues/equipe')  # Modifier pour 'podologues'
    output = output or os.path.join(script_directory, '../json/podologues_content.json')

    podologues = []

    # Lister et trier les dossiers par numéro extrait
    for podologue_name in sorted(os.listdir(directory), key=extract_number_from_folder):
        podologue_path = os.path.join(directory, podologue_name)
        if os.path.isdir(podologue_path):
            podologue = {
                'name': re.sub(r'\d+', '', podologue_name).replace('_', ' ').strip(),  # Supprimer le numéro du nom
                'image': None,
                'pagesjaunes': None,
                'texts': [],
                'pdf': None
            }

            # Parcourir les fichiers du podologue
            for filename in os.listdir(podologue_path):
                file_path = os.path.join(podologue_path, filename)
                if filename == 'pagesjaunes.txt':
                    with open(file_path, 'r', encoding='utf-8') as f:
                        podologue['pagesjaunes'] = f.read().strip()
                elif filename.endswith('.jpg') or filename.endswith('.png'):
                    podologue['image'] = os.path.join(podologue_name, filename)
                elif re.match(r'.*\d+\.txt$', filename):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        num = int(re.findall(r'\d+', filename)[-1])
                        text_name = re.sub(r'\d+\.txt$', '', filename).replace('_', ' ').strip()
                        podologue['texts'].append({
                            'filename': text_name,
                            'content': [line.strip() for line in lines],
                            'order': num
                        })
                elif filename.endswith('.pdf'):
                    podologue['pdf'] = {
                        'path': os.path.join(podologue_name, filename),
                        'name': filename
                    }

            # Trier les fichiers texte par numéro
            podologue['texts'] = sorted(podologue['texts'], key=lambda x: x['order'])

            podologues.append(podologue)

    # Enregistrer la liste des podologues dans le fichier JSON
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(podologues, f, indent=4, ensure_ascii=False)

    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_podologues_json()
