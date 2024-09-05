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
            console.log("Professions loaded:", data);  // Debugging: voir les données chargées

            if (profession) {
                // Trouver la profession dans le JSON
                const professionData = data.find(prof => prof.profession.toLowerCase() === profession.toLowerCase());
                if (professionData) {
                    displayProfessionData(professionData);  // Afficher les données de la profession sélectionnée
                } else {
                    console.error("Profession non trouvée.");
                }
            } else {
                // Si aucune profession n'est spécifiée, afficher toutes les professions
                displayAllProfessions(data);
            }
        })
        .catch(error => {
            console.error('Erreur de chargement des professions:', error);
        });
});

// Fonction pour afficher toutes les professions
function displayAllProfessions(professions) {
    const professionContainer = document.getElementById('professions-container');
    professionContainer.innerHTML = '';  // Nettoyer le contenu

    professions.forEach(professionData => {
        const professionDiv = document.createElement('div');
        professionDiv.classList.add('profession-card');

        const professionTitle = document.createElement('h3');
        professionTitle.textContent = professionData.profession;
        professionDiv.appendChild(professionTitle);

        // Ajouter une liste de personnel
        if (professionData.personnel.length > 0) {
            const personnelList = document.createElement('ul');
            professionData.personnel.forEach(personnel => {
                const listItem = document.createElement('li');
                listItem.textContent = personnel.name;
                personnelList.appendChild(listItem);
            });
            professionDiv.appendChild(personnelList);
        } else {
            const noPersonnel = document.createElement('p');
            noPersonnel.textContent = "Aucun personnel disponible.";
            professionDiv.appendChild(noPersonnel);
        }

        professionContainer.appendChild(professionDiv);
    });
}

// Fonction pour afficher une profession spécifique avec ses personnels
function displayProfessionData(professionData) {
    const professionTitle = document.getElementById('profession-title');
    const personnelContainer = document.getElementById('personnel-container');

    // Titre de la profession
    professionTitle.textContent = professionData.profession;

    // Afficher les personnels et leurs documents
    personnelContainer.innerHTML = '';  // Nettoyer le contenu

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
            listItem.textContent = doc;
            documentList.appendChild(listItem);
        });
        personnelCard.appendChild(documentList);

        personnelContainer.appendChild(personnelCard);
    });
}
