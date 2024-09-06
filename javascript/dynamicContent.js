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

    // Afficher les professionnels et leurs informations
    personnelContainer.innerHTML = '';  // Nettoyer le contenu précédent

    professionData.personnel.forEach(personnel => {
        // Trier les fichiers texte par numéro
        const sortedTexts = personnel.documents
            .filter(doc => doc.endsWith('.txt') && !doc.includes('doctolib')) // Exclure doctolib.txt
            .sort((a, b) => {
                const numA = parseInt(a.match(/\d+/));
                const numB = parseInt(b.match(/\d+/));
                return numA - numB;
            });

        const textsHTML = sortedTexts.map(textFile => {
            const title = textFile.replace(/\d+\.txt$/, '').replace(/_/g, ' ').trim();
            const content = personnel.textContents ? personnel.textContents[textFile] : 'Contenu introuvable.';
            return `
                <h4>${title}</h4>
                <p>${content}</p>
            `;
        }).join('');

        // Si doctolib.txt existe, afficher le bouton pour "Prendre rendez-vous"
        const doctolib = personnel.documents.find(doc => doc === 'doctolib.txt') ? personnel.doctolib : null;
        const pdf = personnel.documents.filter(doc => doc.endsWith('.pdf')).map(pdfFile => {
            return `<p>Document PDF: ${pdfFile}</p>`;
        }).join('');

        const isSinglePersonnel = professionData.personnel.length === 1;
        const collapsibleContentClass = isSinglePersonnel ? 'collapsible-content show' : 'collapsible-content';

        const personnelHTML = `
            <div class="button-section">
                <div class="button-row">
                    <div class="left-text">${personnel.name}</div>
                    <div class="learn-more" onclick="toggleText(this)">En savoir +</div>
                    ${doctolib ? `<a href="${doctolib}" target="_blank"><button class="book-appointment">Prendre rendez-vous</button></a>` : ''}
                </div>
                <div class="${collapsibleContentClass}">
                    <div class="content-wrapper">
                        <img src="/ajoutprofession/${professionData.profession}/${personnel.name}/logo-${personnel.name}.png" alt="Profile Image" />
                        <div class="text-content">
                            ${textsHTML}
                            ${pdf}
                        </div>
                    </div>
                </div>
            </div>
        `;
        personnelContainer.innerHTML += personnelHTML;
    });
}

// Fonction pour afficher/masquer le texte avec gestion du premier clic
function toggleText(element) {
    const content = element.parentElement.nextElementSibling;
    content.classList.toggle('show');
}
