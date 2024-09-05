import os
import json
import re

def get_last_name(full_name):
    return full_name.rsplit(' ', 1)[-1]

def generate_professionals_json(directory=None, output=None):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    directory = directory or os.path.join(script_directory, '../ajoutprofession')
    output = output or os.path.join(script_directory, '../json/professions.json')

    professions = {}

    for profession in os.listdir(directory):
        profession_path = os.path.join(directory, profession)
        if os.path.isdir(profession_path):
            professionals = []

            for professional_name in os.listdir(profession_path):
                professional_path = os.path.join(profession_path, professional_name)
                if os.path.isdir(professional_path):
                    professional = {
                        'name': professional_name.replace('_', ' '),
                        'image': None,
                        'doctolib': None,
                        'texts': [],
                        'pdf': None
                    }

                    for filename in os.listdir(professional_path):
                        file_path = os.path.join(professional_path, filename)
                        if filename == 'doctolib.txt':
                            with open(file_path, 'r', encoding='utf-8') as f:
                                professional['doctolib'] = f.read().strip()
                        elif filename.endswith('.jpg') or filename.endswith('.png'):
                            professional['image'] = os.path.join(professional_name, filename)
                        elif re.match(r'.*\d+\.txt$', filename):
                            with open(file_path, 'r', encoding='utf-8') as f:
                                lines = f.readlines()
                                num = int(re.findall(r'\d+', filename)[-1])
                                text_name = re.sub(r'\d+\.txt$', '', filename)
                                professional['texts'].append({
                                    'filename': text_name,
                                    'content': [line.strip() for line in lines],
                                    'order': num
                                })
                        elif filename.endswith('.pdf'):
                            professional['pdf'] = {
                                'path': os.path.join(professional_name, filename),
                                'name': filename
                            }

                    professional['texts'] = sorted(professional['texts'], key=lambda x: x['order'])
                    professionals.append(professional)

            professions[profession] = sorted(professionals, key=lambda x: get_last_name(x['name']))

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(professions, f, indent=4, ensure_ascii=False)

    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_professionals_json()
