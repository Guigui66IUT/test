document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');

    fetch('../../json/file_list.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            console.log('Fetching file_list.json');
            return response.json();
        })
        .then(files => {
            console.log('Files received:', files);
            const vessel = document.getElementById('vessel');

            // Parcourir chaque clé du fichier JSON
            Object.keys(files).forEach(month => {
                console.log(`Processing files for ${month}`);

                files[month].forEach(filename => {
                    console.log('Processing file:', filename);

                    const card = document.createElement('div');
                    card.classList.add('card');
                    card.onclick = () => downloadPDF(month, filename);

                    const img = document.createElement('img');
                    img.src = month === 'toujours' ? `../../pdf/toujours/${filename}.jpg` : `../../pdf/${month}/${filename}.jpg`;
                    img.alt = filename;
                    img.onerror = () => {
                        console.error(`Image not found: ${img.src}`);
                        img.src = '../../img/placeholder.jpg'; // Chemin de l'image de remplacement si l'image n'est pas trouvée
                    };

                    const p = document.createElement('p');
                    p.textContent = filename;

                    card.appendChild(img);
                    card.appendChild(p);
                    vessel.appendChild(card);

                    console.log('Card created for:', filename);
                });
            });
        })
        .catch(error => {
            console.error('Error fetching file_list.json:', error);
        });
});

function downloadPDF(month, filename) {
    const link = document.createElement('a');
    link.href = month === 'toujours' ? `../../pdf/toujours/${filename}.pdf` : `../../pdf/${month}/${filename}.pdf`;
    link.download = `${filename}.pdf`;
    link.click();
    console.log('Download initiated for:', filename);
}
