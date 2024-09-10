import os
import json
import re

def get_last_name(full_name):
    # Récupérer le dernier mot avant le dernier espace comme nom de famille
    return full_name.rsplit(' ', 1)[-1]

def format_phone_number(phone_number):
    # Ajouter des espaces après chaque groupe de deux chiffres
    return ' '.join([phone_number[i:i+2] for i in range(0, len(phone_number), 2)])

def generate_professions_with_personnel(directory=None, output=None):
    # Obtenir le répertoire du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Définir les chemins par défaut si aucun n'est spécifié
    directory = directory or os.path.join(script_directory, '../ajoutprofession')
    output = output or os.path.join(script_directory, '../json/professions.json')

    professions = []

    # Parcourir les dossiers de profession
    for profession in os.listdir(directory):
        profession_path = os.path.join(directory, profession)

        if os.path.isdir(profession_path):
            personnel_list = []
            profession_logo = None

            # Rechercher un logo de profession
            for file in os.listdir(profession_path):
                if file.endswith('.png') or file.endswith('.jpg'):
                    profession_logo = os.path.join(profession, file).replace('\\', '/')  # Barres obliques pour les URL
                    break

            # Parcourir les dossiers de personnel dans chaque profession
            for personnel in os.listdir(profession_path):
                personnel_path = os.path.join(profession_path, personnel)

                if os.path.isdir(personnel_path):
                    personnel_dict = {
                        'name': personnel.replace('_', ' '),
                        'documents': [],
                        'doctolib': None,  # URL Doctolib ou numéro de téléphone
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
                                content = f.read().strip()
                                # Si le contenu est un numéro de téléphone de 10 chiffres, le formater
                                if re.match(r'^\d{10}$', content):
                                    personnel_dict['doctolib'] = format_phone_number(content)
                                else:
                                    personnel_dict['doctolib'] = content  # Si ce n'est pas un numéro de téléphone, garder tel quel

                        # Lire et stocker les fichiers d'images
                        elif filename.endswith('.jpg') or filename.endswith('.png'):
                            personnel_dict['image'] = os.path.join(personnel, filename).replace('\\', '/')  # Barres obliques pour les URL

                        # Traiter les fichiers texte numérotés (1.txt, 2.txt, etc.)
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

                        # Lire les fichiers PDF
                        elif filename.endswith('.pdf'):
                            personnel_dict['pdf'] = {
                                'path': os.path.join('..', '..', '..', 'ajoutprofession', profession, personnel, filename).replace('\\', '/'),  # Chemin complet
                                'name': filename
                            }

                    # Trier les fichiers texte par numéro
                    personnel_dict['texts'] = sorted(personnel_dict['texts'], key=lambda x: x['order'])

                    personnel_list.append(personnel_dict)

            # Trier les personnes par nom de famille
            personnel_list = sorted(personnel_list, key=lambda x: get_last_name(x['name']))

            professions.append({
                'profession': profession.replace('_', ' '),
                'logo': profession_logo,  # Ajouter le logo de la profession
                'personnel': personnel_list
            })

    # Enregistrer la liste des professions avec leur personnel dans professions.json
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(professions, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    generate_professions_with_personnel()
