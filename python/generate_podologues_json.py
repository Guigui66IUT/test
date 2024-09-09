import os
import json
import re

def get_folder_number(folder_name):
    """
    Récupérer le numéro dans le nom du dossier, s'il existe.
    Par exemple, pour "Podologue_1", il renverra 1.
    Si aucun numéro n'est trouvé, renvoyer un nombre élevé pour qu'il soit trié en dernier.
    """
    match = re.search(r'(\d+)', folder_name)
    if match:
        return int(match.group(1))
    return float('inf')  # Retourner un grand nombre si aucun numéro n'est trouvé

def remove_number_from_name(folder_name):
    """
    Enlever le numéro du nom du podologue.
    Par exemple, "Podologue_1" devient "Podologue".
    """
    return re.sub(r'_\d+', '', folder_name).replace('_', ' ').strip()

def generate_podologues_json(directory=None, output=None):
    # Obtenir le répertoire du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir les chemins par défaut si aucun n'est spécifié
    directory = directory or os.path.join(script_directory, '../podologues/equipe')  # Modifier pour 'podologues'
    output = output or os.path.join(script_directory, '../json/podologues_content.json')

    podologues = []

    for podologue_name in os.listdir(directory):
        podologue_path = os.path.join(directory, podologue_name)
        if os.path.isdir(podologue_path):
            podologue = {
                'name': remove_number_from_name(podologue_name),  # Enlever le numéro du nom
                'image': None,
                'pagesjaunes': None,
                'texts': [],
                'pdf': None
            }

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
                        text_name = re.sub(r'\d+\.txt$', '', filename)  # Supprime les chiffres et .txt
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

    # Trier les podologues par numéro dans le nom du dossier
    podologues = sorted(podologues, key=lambda x: get_folder_number(x['name']))

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(podologues, f, indent=4, ensure_ascii=False)

    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_podologues_json()
