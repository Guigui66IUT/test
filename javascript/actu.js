
document.addEventListener('DOMContentLoaded', () => {
    fetch('../file_list.json')
        .then(response => response.json())
        .then(files => {
            const vessel = document.getElementById('vessel');

			alert(files);

            files.forEach(filename => {
                const card = document.createElement('div');
                card.classList.add('card');
                card.onclick = () => downloadPDF(filename);

                const img = document.createElement('img');
                img.src = `../pdf/${filename}.jpg`; // Chemin de l'image
                img.alt = filename;

                const p = document.createElement('p');
                p.textContent = filename;

                card.appendChild(img);
                card.appendChild(p);
                vessel.appendChild(card);
            });
        });
});

function downloadPDF(filename) {
    const link = document.createElement('a');
    link.href = `../pdf/${filename}.pdf`;
    link.download = `${filename}.pdf`;
    link.click();
}
