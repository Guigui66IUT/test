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
    """ Extrait le chemin des images du fichier HTML. """
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        slider_container = soup.find(class_='slider-container')
        if slider_container and slider_container.has_attr('data-img-path'):
            return slider_container['data-img-path']
        return None

def generate_images_json(html_file, output_dir, img_path):
    """ Génère un fichier JSON contenant les images pour un fichier HTML spécifique. """
    images = []

    img_path_full = os.path.join(img_path.replace('/', os.sep))  # Utilisation du chemin fourni

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

if __name__ == "__main__":
    # Définir les chemins absolus pour chaque fichier HTML et leurs images respectives
    base_dir = os.path.dirname(os.path.abspath(__file__))

    html_files_and_images = [
        (os.path.join(base_dir, '..', 'index.html'), 'img/accueil/slideraccueil/'),  # Images pour l'index
        (os.path.join(base_dir, '..', 'html', 'profession', 'podo', 'podo.html'), 'img/podo/sliderpodo/'),  # Images pour Podo
        (os.path.join(base_dir, '..', 'html', 'profession', 'kine', 'kine.html'), 'img/kine/sliderkine/'),  # Images pour Kine
        (os.path.join(base_dir, '..', 'html', 'profession', 'infi', 'infi.html'), 'img/infi/sliderinfi/')  # Images pour Infi
    ]
    
    output_dir = os.path.join(base_dir, '..', 'json')

    # Boucle pour générer les fichiers JSON d'images pour chaque HTML
    for html_file, img_path in html_files_and_images:
        generate_images_json(html_file, output_dir, img_path)