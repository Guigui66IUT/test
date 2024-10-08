window.onload = function() {
    const pdfContainer = document.getElementById('pdf-container');
    
    // Charger le fichier JSON qui contient le nom du PDF
    fetch('/json/pdf_info.json')  // Le fichier JSON est maintenant dans le dossier "json"
        .then(response => response.json())
        .then(data => {
            const pdfFilename = data.pdf_filename;
            
            // Créer l'élément embed pour afficher le PDF
            const embed = document.createElement('embed');
            embed.src = `/projet de sante/${pdfFilename}`;  // Utiliser le nom du fichier PDF récupéré
            embed.type = 'application/pdf';
            embed.width = '100%';
            
            // Ajuster la hauteur pour qu'elle prenne toute la hauteur de l'écran
            embed.style.height = `${window.innerHeight}px`;

            // Ajouter un écouteur pour redimensionner la hauteur si l'utilisateur redimensionne la fenêtre
            window.addEventListener('resize', function() {
                embed.style.height = `${window.innerHeight}px`;
            });

            // Ajouter l'élément embed au conteneur
            pdfContainer.appendChild(embed);
        })
        .catch(error => {
            console.error('Erreur lors de la récupération du fichier PDF:', error);
        });
};
