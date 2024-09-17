import os
import json
import re

def get_last_name(full_name):
    return full_name.rsplit(' ', 1)[-1]

def format_phone_number(phone_number):
    return ' '.join([phone_number[i:i+2] for i in range(0, len(phone_number), 2)])

def generate_professions_with_personnel(directory=None, output=None):
    script_directory = os.path.dirname(os.path.abspath(__file__))

    directory = directory or os.path.join(script_directory, '../ajoutprofession')
    output = output or os.path.join(script_directory, '../json/professions.json')

    professions = []

    for subdirectory in ['ajout_med', 'ajout_para-med']:
        subdirectory_path = os.path.join(directory, subdirectory)

        for profession in os.listdir(subdirectory_path):
            profession_path = os.path.join(subdirectory_path, profession)

            if os.path.isdir(profession_path):
                personnel_list = []
                profession_logo = None

                for file in os.listdir(profession_path):
                    if file.endswith('.png') or file.endswith('.jpg'):
                        profession_logo = os.path.join(subdirectory, profession, file).replace('\\', '/')
                        break

                for personnel in os.listdir(profession_path):
                    personnel_path = os.path.join(profession_path, personnel)

                    if os.path.isdir(personnel_path):
                        personnel_dict = {
                            'name': personnel.replace('_', ' '),
                            'documents': [],
                            'doctolib': None,
                            'texts': [],
                            'pdf': None,
                            'image': None
                        }

                        for filename in os.listdir(personnel_path):
                            file_path = os.path.join(personnel_path, filename)

                            if filename in ['doctolib.txt', 'pagesjaunes.txt']:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    content = f.read().strip()
                                    if re.match(r'^\d{10}$', content):
                                        personnel_dict['doctolib'] = format_phone_number(content)
                                    else:
                                        personnel_dict['doctolib'] = content

                            elif filename.endswith('.jpg') or filename.endswith('.png'):
                                personnel_dict['image'] = os.path.join(subdirectory, profession, personnel, filename).replace('\\', '/')

                            elif re.match(r'.*\d+\.txt$', filename):
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    lines = f.readlines()
                                    num = int(re.findall(r'\d+', filename)[-1])
                                    text_name = re.sub(r'\d+\.txt$', '', filename).replace('_', ' ').strip()
                                    personnel_dict['texts'].append({
                                        'filename': text_name,
                                        'content': [line.strip() for line in lines],
                                        'order': num
                                    })

                            elif filename.endswith('.pdf'):
                                personnel_dict['pdf'] = {
                                    'path': os.path.join('ajoutprofession', subdirectory, profession, personnel, filename).replace('\\', '/'),
                                    'name': filename
                                }

                        personnel_dict['texts'] = sorted(personnel_dict['texts'], key=lambda x: x['order'])
                        personnel_list.append(personnel_dict)

                personnel_list = sorted(personnel_list, key=lambda x: get_last_name(x['name']))

                profession_type = 'general' if subdirectory == 'ajout_med' else 'specific'

                professions.append({
                    'profession': profession.replace('_', ' '),
                    'logo': profession_logo,
                    'personnel': personnel_list,
                    'type': profession_type
                })

    with open(output, 'w', encoding='utf-8') as f:
        json.dump(professions, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    generate_professions_with_personnel()
