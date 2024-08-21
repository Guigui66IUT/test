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

def generate_images_json(img_path, output):
    images = []
    
    # Parcourir les fichiers dans le répertoire spécifié
    if os.path.exists(img_path):
        for filename in os.listdir(img_path):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                images.append(filename)
    
        # Écrire la liste des fichiers dans un fichier JSON
        with open(output, 'w', encoding='utf-8') as json_file:
            json.dump(images, json_file, indent=4)
            
        print(f'Fichier {output} généré avec succès.')
    else:
        print(f"Le chemin {img_path} n'existe pas.")

if __name__ == "__main__":
    # Si 'index.html' est dans le répertoire parent du script, ajustez le chemin ainsi
    html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')
    
    img_path = extract_image_path_from_html(html_file)
    
    if img_path:
        # Construire le chemin complet basé sur le chemin récupéré depuis le HTML
        img_path_full = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', img_path.replace('/', os.sep))
        output = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'json', 'slider_images.json')
        generate_images_json(img_path_full, output)
    else:
        print("Chemin des images non trouvé dans le fichier HTML.")
