document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const profession = urlParams.get('profession');

    fetch('/json/professions.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur lors du chargement des professions.');
            }
            return response.json();
        })
        .then(data => {
            // Charger dynamiquement la profession sélectionnée
            if (profession) {
                const professionData = data.find(prof => prof.profession.toLowerCase() === profession.toLowerCase());
                if (professionData) {
                    displayProfessionData(professionData);
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
    const professionLogo = document.getElementById('profession-logo');
    const professionTitle = document.getElementById('profession-title');
    const personnelContainer = document.getElementById('personnel-container');

    // Titre de la profession
    professionTitle.textContent = professionData.profession;

    // Afficher les personnels et leurs documents
    professionData.personnel.forEach(personnel => {
        const personnelCard = document.createElement('div');
        personnelCard.classList.add('personnel-card');

        // Nom du personnel
        const personnelName = document.createElement('h3');
        personnelName.textContent = personnel.name;
        personnelCard.appendChild(personnelName);

        // Liste des documents
        const documentList = document.createElement('ul');
        personnel.documents.forEach(doc => {
            const listItem = document.createElement('li');
            listItem.textContent = doc;
            documentList.appendChild(listItem);
        });
        personnelCard.appendChild(documentList);

        personnelContainer.appendChild(personnelCard);
    });
}
