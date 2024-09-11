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

import os
import json
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
        # Construct path from 'img/' directory
        project_root = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))  # Navigate to project root
        img_path_full = os.path.join(project_root, img_path.replace('/', os.sep))  # Full image path
        
        images = []

        if os.path.exists(img_path_full):
            for filename in os.listdir(img_path_full):
                if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    images.append(filename)

            # Create the output JSON file in the 'json' directory
            output = os.path.join(output_dir, f'{os.path.basename(html_file).replace(".html", "")}_images.json')
            
            # Write image filenames to JSON
            with open(output, 'w', encoding='utf-8') as json_file:
                json.dump(images, json_file, indent=4)
                
            print(f'Fichier {output} généré avec succès.')
        else:
            print(f"Le chemin {img_path_full} n'existe pas.")
    else:
        print("Chemin des images non trouvé dans le fichier HTML.")

if __name__ == "__main__":
    # Define paths to the HTML files
    base_dir = os.path.dirname(os.path.abspath(__file__))

    html_files = [
        os.path.join(base_dir, '..', 'index.html'),  # Images for index.html
        os.path.join(base_dir, '..', 'html', 'profession', 'podo', 'podo.html'),  # Images for Podo
        os.path.join(base_dir, '..', 'html', 'profession', 'kine', 'kine.html'),  # Images for Kine
        os.path.join(base_dir, '..', 'html', 'profession', 'infi', 'infi.html')  # Images for Infi
    ]
    
    # Set output directory for JSON files
    output_dir = os.path.join(base_dir, '..', 'json')

    # Generate JSON for each HTML file
    for html_file in html_files:
        generate_images_json(html_file, output_dir)
