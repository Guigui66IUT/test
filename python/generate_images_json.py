import os
import sys
import subprocess
import json  # Assurez-vous que json est bien importé

# Fonction pour installer un package
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

# Vérifier et installer les packages nécessaires
install_and_import('bs4')

from bs4 import BeautifulSoup

def extract_image_path_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        slider_container = soup.find(class_='slider-container')
        if slider_container and slider_container.has_attr('data-img-path'):
            return slider_container['data-img-path']
        return None

def generate_images_json(html_file, output_dir):
    img_path = extract_image_path_from_html(html_file)
    
    if img_path:
        # Construire le chemin complet basé sur le répertoire parent du dossier python
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Dossier 'python'
        project_root = os.path.dirname(base_dir)  # Remonte au niveau du projet (dossier 'Site')
        img_path_full = os.path.join(project_root, img_path.replace('/', os.sep))  # Chemin complet vers le dossier d'images

        images = []

        if os.path.exists(img_path_full):
            for filename in os.listdir(img_path_full):
                if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    images.append(filename)

            # Construire le nom de sortie en fonction du fichier HTML
            output = os.path.join(output_dir, f'{os.path.basename(html_file).replace(".html", "")}_images.json')
            
            # Écrire la liste des fichiers dans un fichier JSON
            with open(output, 'w', encoding='utf-8') as json_file:
                json.dump(images, json_file, indent=4)
                
            print(f'Fichier {output} généré avec succès.')
        else:
            print(f"Le chemin {img_path_full} n'existe pas.")
    else:
        print("Chemin des images non trouvé dans le fichier HTML.")

if __name__ == "__main__":
    # Définir les chemins relatifs pour chaque fichier HTML
    html_files = [
        os.path.join('..', 'index.html'),  # Pour les images de l'index
        os.path.join('..', 'html', 'profession', 'podo', 'podo.html'),  # Pour les images de Podo
        os.path.join('..', 'html', 'profession', 'kine', 'kine.html'),  # Pour les images de Kine
        os.path.join('..', 'html', 'profession', 'infi', 'infi.html')  # Pour les images de Infi
    ]
    
    # Dossier de sortie pour les fichiers JSON
    output_dir = os.path.join('..', 'json')
    
    # Créer le dossier de sortie s'il n'existe pas
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for html_file in html_files:
        generate_images_json(html_file, output_dir)
