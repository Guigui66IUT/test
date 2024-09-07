import os
import json
import re

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
            profession_logo = None

            # Rechercher un logo de profession
            for file in os.listdir(profession_path):
                if file.startswith('logo') and (file.endswith('.png') or file.endswith('.jpg')):
                    profession_logo = os.path.join(profession, file).replace('/', '\\')  # Utiliser les barres obliques inverses
                    break

            # Parcourir les dossiers de personnel dans chaque profession
            for personnel in os.listdir(profession_path):
                personnel_path = os.path.join(profession_path, personnel)

                if os.path.isdir(personnel_path):
                    personnel_dict = {
                        'name': personnel.replace('_', ' '),
                        'documents': [],
                        'doctolib': None,  # URL Doctolib
                        'texts': [],  # Contiendra les textes triés par numéro
                        'pdf': None,  # Pour stocker les informations sur le PDF
                        'image': None  # Pour stocker les informations sur l'image
                    }

                    # Lire les fichiers du personnel
                    for filename in os.listdir(personnel_path):
                        file_path = os.path.join(personnel_path, filename)

                        # Lire le fichier doctolib.txt
                        if filename == 'doctolib.txt':
                            with open(file_path, 'r', encoding='utf-8') as f:
                                personnel_dict['doctolib'] = f.read().strip()

                        # Lire et stocker les fichiers d'images
                        elif filename.endswith('.jpg') or filename.endswith('.png'):
                            personnel_dict['image'] = os.path.join(personnel, filename).replace('/', '\\')

                        # Traiter les fichiers texte numérotés (1.txt, 2.txt, etc.)
                        elif re.match(r'.*\d+\.txt$', filename):
                            with open(file_path, 'r', encoding='utf-8') as f:
                                lines = f.readlines()
                                # Extraire le numéro du fichier texte
                                num = int(re.findall(r'\d+', filename)[-1])
                                # Supprimer le numéro et l'extension .txt du nom de fichier
                                text_name = re.sub(r'\d+\.txt$', '', filename).replace('_', ' ').strip()
                                # Ajouter le contenu et le numéro dans la liste des textes
                                personnel_dict['texts'].append({
                                    'filename': text_name,
                                    'content': [line.strip() for line in lines],
                                    'order': num
                                })

                        # Lire les fichiers PDF
                        elif filename.endswith('.pdf'):
                            personnel_dict['pdf'] = {
                                'path': os.path.join(personnel, filename).replace('/', '\\'),
                                'name': filename
                            }

                    # Trier les fichiers texte par numéro
                    personnel_dict['texts'] = sorted(personnel_dict['texts'], key=lambda x: x['order'])

                    personnel_list.append(personnel_dict)

            professions.append({
                'profession': profession.replace('_', ' '),
                'logo': profession_logo,  # Ajouter le logo de la profession
                'personnel': personnel_list
            })

    # Enregistrer la liste des professions avec leur personnel dans professions.json
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(professions, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    update_professions_with_personnel()
