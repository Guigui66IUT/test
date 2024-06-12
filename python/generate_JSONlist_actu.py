import os
import json

def generate_JSONlist_actu(directory='../pdf', output='../json/file_list.json'):
    # Récupérer tous les fichiers PDF dans le répertoire spécifié
    pdf_files = [f.replace('.pdf', '') for f in os.listdir(directory) if f.endswith('.pdf')]
    
    # Écrire la liste des fichiers dans un fichier JSON
    with open(output, 'w') as json_file:
        json.dump(pdf_files, json_file, indent=4)
        
    print(f'Fichier {output} généré avec succès.')

if __name__ == "__main__":
    generate_JSONlist_actu()
