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
        # Construire le chemin relatif au répertoire racine du projet 'Site'
        project_root = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))  # Remonter de deux niveaux pour aller à 'Site'
        img_path_full = os.path.join(project_root, 'img', img_path)  # S'assurer de commencer à partir du dossier 'img'

        images = []

        if os.path.exists(img_path_full):
            for filename in os.listdir(img_path_full):
                if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    images.append(filename)

            # Créer le fichier JSON de sortie dans le répertoire 'json'
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
    # Définir les chemins pour chaque fichier HTML
    base_dir = os.path.dirname(os.path.abspath(__file__))

    html_files = [
        os.path.join(base_dir, '../index.html'),  # Pour les images de l'index
        os.path.join(base_dir, '../html/profession/podo/podo.html'),  # Pour les images de Podo
        os.path.join(base_dir, '../html/profession/kine/kine.html'),  # Pour les images de Kine
        os.path.join(base_dir, '../html/profession/infi/infi.html')  # Pour les images de Infi
    ]
    
    # Définir le répertoire de sortie pour les fichiers JSON
    output_dir = os.path.join(base_dir, '..', 'json')

    # Générer les fichiers JSON pour chaque fichier HTML
    for html_file in html_files:
        generate_images_json(html_file, output_dir)