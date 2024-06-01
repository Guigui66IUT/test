import os
import json
import re

def generate_medecins_json(directory='medecins', output='medecins_content.json'):
    medecins = []

    for medecin_name in os.listdir(directory):
        medecin_path = os.path.join(directory, medecin_name)
        if os.path.isdir(medecin_path):
            medecin = {
                'name': medecin_name.replace('_', ' '),
                'image': None,
                'doctolib': None,
                'texts': [],
                'pdf': None
            }

            for filename in os.listdir(medecin_path):
                file_path = os.path.join(medecin_path, filename)
                if filename == 'doctolib.txt':
                    with open(file_path, 'r') as f:
                        medecin['doctolib'] = f.read().strip()
                elif filename.endswith('.jpg') or filename.endswith('.png'):
                    medecin['image'] = file_path
                elif re.match(r'.*\d+\.txt$', filename):
                    with open(file_path, 'r') as f:
                        lines = f.readlines()
                        num = int(re.findall(r'\d+', filename)[-1])
                        text_name = re.sub(r'\d+\.txt$', '', filename)  # Supprime les chiffres et .txt
                        medecin['texts'].append({
                            'filename': text_name,
                            'content': [line.strip() for line in lines],
                            'order': num
                        })
                elif filename.endswith('.pdf'):
                    medecin['pdf'] = {
                        'path': file_path,
                        'name': filename
                    }

            # Trier les fichiers texte par numéro
            medecin['texts'] = sorted(medecin['texts'], key=lambda x: x['order'])

            medecins.append(medecin)

    with open(output, 'w') as f:
        json.dump(medecins, f, indent=4)

if __name__ == "__main__":
    generate_medecins_json()
