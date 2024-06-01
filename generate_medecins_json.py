import os
import json

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
                elif filename.startswith('text') and filename.endswith('.txt'):
                    with open(file_path, 'r') as f:
                        medecin['texts'].append(f.read().strip())
                elif filename.endswith('.pdf'):
                    medecin['pdf'] = {
                        'path': file_path,
                        'name': filename
                    }

            medecins.append(medecin)

    with open(output, 'w') as f:
        json.dump(medecins, f, indent=4)

if __name__ == "__main__":
    generate_medecins_json()
