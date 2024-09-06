document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const profession = urlParams.get('profession');

    // Charger le fichier JSON des professions
    fetch('/json/professions.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur lors du chargement des professions.');
            }
            return response.json();
        })
        .then(data => {
            if (profession) {
                // Trouver la profession dans le JSON
                const professionData = data.find(prof => prof.profession.toLowerCase() === profession.toLowerCase());
                if (professionData) {
                    displayProfessionData(professionData);  // Afficher les données de la profession sélectionnée
                } else {
                    console.error("Profession non trouvée.");
                }
            }
        })
        .catch(error => {
            console.error('Erreur de chargement des professions:', error);
        });
});

function displayProfessionData(professionData) {
    const professionTitle = document.getElementById('profession-title');
    const personnelContainer = document.getElementById('profession-container');

    // Vérifier que les éléments DOM existent
    if (!professionTitle || !personnelContainer) {
        console.error("Les éléments DOM pour l'affichage des professionnels ne sont pas trouvés.");
        return;
    }

    // Titre de la profession
    professionTitle.textContent = professionData.profession;

    // Vérifier s'il y a du personnel pour cette profession
    if (professionData.personnel.length === 0) {
        personnelContainer.innerHTML = "<p>Aucun professionnel disponible pour cette profession.</p>";
        return;
    }

    // Afficher les professionnels et leurs documents
    personnelContainer.innerHTML = '';  // Nettoyer le contenu précédent

    professionData.personnel.forEach(personnel => {
        const personnelCard = document.createElement('div');
        personnelCard.classList.add('personnel-card');

        const personnelName = document.createElement('h3');
        personnelName.textContent = personnel.name;
        personnelCard.appendChild(personnelName);

        // Liste des documents
        const documentList = document.createElement('ul');
        personnel.documents.forEach(doc => {
            const listItem = document.createElement('li');

            // Vérifier le type de fichier
            if (doc.endsWith('.pdf') || doc.endsWith('.txt')) {
                // Créer un lien pour télécharger les PDF ou TXT
                const link = document.createElement('a');
                link.href = `/ajoutprofession/${professionData.profession}/${personnel.name}/${doc}`;
                link.textContent = `Télécharger ${doc}`;
                link.target = '_blank';  // Ouvre le document dans un nouvel onglet
                listItem.appendChild(link);
            } else if (doc.endsWith('.png') || doc.endsWith('.jpg') || doc.endsWith('.jpeg')) {
                // Afficher une image pour les fichiers PNG/JPG
                const img = document.createElement('img');
                img.src = `/ajoutprofession/${professionData.profession}/${personnel.name}/${doc}`;
                img.alt = doc;
                img.style.maxWidth = '150px';  // Limiter la taille de l'image
                listItem.appendChild(img);
            } else {
                // Pour tout autre type de fichier (par exemple, doc inconnu)
                listItem.textContent = doc;
            }

            documentList.appendChild(listItem);
        });
        personnelCard.appendChild(documentList);

        personnelContainer.appendChild(personnelCard);
    });
}
