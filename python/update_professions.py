import os
import json

def update_professions_with_personnel():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    ajoutprofession_path = os.path.join(base_path, 'ajoutprofession')
    json_path = os.path.join(base_path, 'json', 'professions.json')

    professions = []

    # Parcourir les dossiers de profession
    for profession in os.listdir(ajoutprofession_path):
        profession_path = os.path.join(ajoutprofession_path, profession)

        if os.path.isdir(profession_path):
            personnel_list = []
            # Parcourir les dossiers de personnel dans chaque profession
            for personnel in os.listdir(profession_path):
                personnel_path = os.path.join(profession_path, personnel)

                if os.path.isdir(personnel_path):
                    # Ajouter chaque personnel dans la liste
                    personnel_dict = {
                        'name': personnel.replace('_', ' '),
                        'documents': []
                    }

                    # Ajouter les documents du personnel (txt, pdf, images)
                    for file in os.listdir(personnel_path):
                        if file.endswith('.txt') or file.endswith('.pdf') or file.endswith('.png') or file.endswith('.jpg'):
                            personnel_dict['documents'].append(file)

                    personnel_list.append(personnel_dict)

            # Ajouter la profession et son personnel dans la liste des professions
            professions.append({
                'profession': profession.replace('_', ' '),
                'personnel': personnel_list
            })

    # Enregistrer la liste des professions avec leur personnel dans professions.json
    with open(json_path, 'w') as f:
        json.dump(professions, f, indent=4)

    print(f'Updated professions.json with {len(professions)} professions and personnel.')

if __name__ == '__main__':
    update_professions_with_personnel()
