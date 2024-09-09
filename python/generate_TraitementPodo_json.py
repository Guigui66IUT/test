
import os
import json
import re

def generate_traitement_podo_files(directory=None, output_json=None):
    # Obtain the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Set default paths if none are specified
    directory = directory or os.path.join(script_directory, '../podologues/traitement/')

    # Path for the JSON file
    output_json = output_json or os.path.join(script_directory, '../json/traitementpodo_content.json')

    traitements = []

    # Read descriptions from text files and gather JSON data
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            # Extract the treatment name and number
            match = re.match(r'^(.*)_(\d+)\.jpg$', filename)
            if match:
                treatment_name = match.group(1).replace('_', ' ').upper()
                order = int(match.group(2))
                text_filename = f"{treatment_name.lower().replace(' ', '_')}.txt"
                text_filepath = os.path.join(directory, text_filename)

                # Read the content of the text file
                try:
                    with open(text_filepath, 'r', encoding='utf-8') as file:
                        description_text = file.read()
                except FileNotFoundError:
                    description_text = "Description not found."
                
                # Append data for JSON
                traitement = {
                    'name': treatment_name,
                    'image': filename,
                    'order': order,
                    'txt_file': text_filename,
                    't': description_text
                }
                traitements.append(traitement)

    # Sort treatments by order
    traitements = sorted(traitements, key=lambda x: x['order'])

    # Write data to a JSON file
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(traitements, f, indent=4, ensure_ascii=False)
    
    print(f'JSON file {output_json} successfully generated.')
    print(f'Description files confirmed in {directory}.')

if __name__ == "__main__":
    generate_traitement_podo_files()
