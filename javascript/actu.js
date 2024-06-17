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

            files.forEach(filename => {
                console.log('Processing file:', filename);

                const card = document.createElement('div');
                card.classList.add('card');
                card.onclick = () => downloadPDF(filename);

                const img = document.createElement('img');
                img.src = `../../pdf/${filename}.jpg`; // Chemin de l'image
                img.alt = filename;

                const p = document.createElement('p');
                p.textContent = filename;

                card.appendChild(img);
                card.appendChild(p);
                vessel.appendChild(card);

                console.log('Card created for:', filename);
            });
        })
        .catch(error => {
            console.error('Error fetching file_list.json:', error);
        });
});

function downloadPDF(filename) {
    const link = document.createElement('a');
    link.href = `../../pdf/${filename}.pdf`;
    link.download = `${filename}.pdf`;
    link.click();
    console.log('Download initiated for:', filename);
}
