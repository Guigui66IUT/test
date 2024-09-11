import os
import json

def get_pdf_filename(pdf_directory='../projet de sante', output_directory='../json'):
    # Rechercher tous les fichiers PDF dans le dossier
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
    
    if pdf_files:
        # Prendre le premier PDF trouvé
        pdf_file = pdf_files[0]
        print(f"Fichier PDF trouvé : {pdf_file}")
        
        # Sauvegarder le nom du fichier PDF dans un fichier JSON
        pdf_info = {
            'pdf_filename': pdf_file
        }
        
        # Construire le chemin pour sauvegarder le JSON dans le dossier json
        output_json = os.path.join(output_directory, 'pdf_info.json')
        
        # Vérifier si le dossier de sortie existe, sinon le créer
        os.makedirs(output_directory, exist_ok=True)
        
        with open(output_json, 'w', encoding='utf-8') as json_file:
            json.dump(pdf_info, json_file, indent=4)
        
        print(f"Nom du fichier PDF sauvegardé dans {output_json}")
    else:
        print("Aucun fichier PDF trouvé dans le dossier.")

if __name__ == "__main__":
    get_pdf_filename()
