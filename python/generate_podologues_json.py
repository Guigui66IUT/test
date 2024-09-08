import os
import json
import re

def get_last_name(full_name):
    # Récupérer le dernier mot avant le dernier espace comme nom de famille
    return full_name.rsplit(' ', 1)[-1]

def generate_podologues_json(directory=None, output=None):
    # Obtenir le répertoire du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir les chemins par défaut si aucun n'est spécifié
    directory = directory or os.path.join(script_directory, '../podologues/equipe')  # Modifier pour 'podologues'
    output = output or os.path.join(script_directory, '../../json/podologues_content.json')

    # Vérifier si le répertoire de sortie existe, sinon le créer
    output_dir = os.path.dirname(output)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Création du répertoire : {output_dir}")

    podologues = []

    for podologue_name in os.listdir(directory):
        podologue_path = os.path.join(directory, podologue_name)
        if os.path.isdir(podologue_path):
            podologue = {
                'name': podologue_name.replace('_', ' '),
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

    # Trier les podologues par nom de famille
    podologues = sorted(podologues, key=lambda x: get_last_name(x['name']))

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(podologues, f, indent=4, ensure_ascii=False)

    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_podologues_json()
