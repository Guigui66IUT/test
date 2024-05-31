import os

def generate_medecins_html(directory='medecins', output='medecins_content.html'):
    medecins = []

    for medecin_name in os.listdir(directory):
        medecin_path = os.path.join(directory, medecin_name)
        if os.path.isdir(medecin_path):
            medecin = {
                'name': medecin_name.replace('_', ' '),
                'image': None,
                'doctolib': None,
                'texts': [],
                'pdf': None
            }

            for filename in os.listdir(medecin_path):
                file_path = os.path.join(medecin_path, filename)
                if filename == 'doctolib.txt':
                    with open(file_path, 'r') as f:
                        medecin['doctolib'] = f.read().strip()
                elif filename.endswith('.jpg') or filename.endswith('.png'):
                    medecin['image'] = file_path
                elif filename.startswith('text') and filename.endswith('.txt'):
                    with open(file_path, 'r') as f:
                        medecin['texts'].append(f.read().strip())
                elif filename.endswith('.pdf'):
                    medecin['pdf'] = file_path

            medecins.append(medecin)

    html_content = '<div class="personnage">\n'
    for medecin in medecins:
        html_content += f'''
        <div class="button-section">
            <div class="button-row">
                <div class="left-text">{medecin['name']}</div>
                <div class="learn-more" onclick="toggleText(this)">En savoir +</div>
                <a href="{medecin['doctolib']}" target="_blank">
                    <button class="book-appointment">Prendre rendez-vous</button>
                </a>
            </div>
            <div class="collapsible-content">
                <div class="content-wrapper">
                    <img src="{medecin['image']}" alt="Profile Image" />
                    <div class="text-content">
                        {''.join([f'<p>{text}</p>' for text in medecin['texts']])}
                        {f'<a href="{medecin["pdf"]}" download class="download-link">Autre</a>' if medecin['pdf'] else ''}
                    </div>
                </div>
            </div>
        </div>
        '''
    html_content += '</div>\n'

    with open(output, 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_medecins_html()
