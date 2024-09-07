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
            console.log("Données chargées :", data);
            if (profession) {
                // Trouver la profession dans le JSON
                const professionData = data.find(prof => prof.profession.toLowerCase() === profession.toLowerCase());
                console.log("Données de la profession trouvée :", professionData);
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
    const professionTitle = document.getElementById('profession-title');
    const professionLogo = document.getElementById('profession-logo');
    const personnelContainer = document.getElementById('profession-container');

    // Vérifier les éléments DOM
    console.log('Profession Title Element:', professionTitle);
    console.log('Personnel Container Element:', personnelContainer);
    console.log('Profession Logo Element:', professionLogo);

    if (!professionTitle || !personnelContainer || !professionLogo) {
        console.error("Les éléments DOM pour l'affichage des professionnels ne sont pas trouvés.");
        return;
    }

    // Titre de la profession
    professionTitle.textContent = professionData.profession;

    // Afficher le logo de la profession
    if (professionData.logo) {
        console.log('Logo de la profession:', professionData.logo);
        professionLogo.src = encodeURIComponent(professionData.logo).replace(/%2F/g, '/');
        professionLogo.alt = `Logo ${professionData.profession}`;
        professionLogo.style.display = 'block';
    } else {
        console.warn("Aucun logo trouvé pour la profession.");
    }

    // Afficher les professionnels et leurs informations
    personnelContainer.innerHTML = '';  // Nettoyer le contenu précédent

    if (professionData.personnel.length === 0) {
        personnelContainer.innerHTML = "<p>Aucun professionnel disponible pour cette profession.</p>";
        return;
    }

    professionData.personnel.forEach(personnel => {
        console.log("Traitement du personnel :", personnel);

        // Vérification du contenu de textContents
        console.log("Contenu des fichiers textes du personnel:", personnel.textContents);

        // Trier les fichiers texte par numéro
        const sortedTexts = personnel.documents
            .filter(doc => doc.endsWith('.txt') && !doc.includes('doctolib'))
            .sort((a, b) => {
                const numA = parseInt(a.match(/\d+/));
                const numB = parseInt(b.match(/\d+/));
                return numA - numB;
            });

        
        // Vérification des fichiers PDF et génération des liens de téléchargement
        const pdf = personnel.pdf ? `<a href="../../${personnel.pdf.path}" download="${personnel.pdf.name}" class="download-link">Autre</a>` : '';

        // Génération du HTML pour les fichiers textes
        const textsHTML = personnel.texts.map(text => `
            <h4>${text.filename}</h4>
            <ul>
                ${text.content.map(line => `<li>${line}</li>`).join('')}
            </ul>
        `).join('');


        // // Génération du HTML pour les textes
        // const textsHTML = sortedTexts.map(textFile => {
        //     const title = textFile.replace(/\d+\.txt$/, '').replace(/_/g, ' ').trim();
        //     const content = personnel.textContents ? personnel.textContents[textFile] : 'Contenu introuvable.';
        //     console.log(`Fichier texte: ${textFile}, Contenu: ${content}`);
        //     return `
        //         <h4>${title}</h4>
        //         <p>${content}</p>
        //     `;
        // }).join('');

        // Si doctolib.txt existe, afficher le bouton pour "Prendre rendez-vous"
        const doctolib = personnel.doctolib ? personnel.doctolib : null;
        // const pdf = personnel.documents.filter(doc => doc.endsWith('.pdf')).map(pdfFile => {
        //     return `<p>Document PDF: ${pdfFile}</p>`;
        // }).join('');





        

        const isSinglePersonnel = professionData.personnel.length === 1;
        const collapsibleContentClass = isSinglePersonnel ? 'collapsible-content show' : 'collapsible-content';

        const personnelHTML = `
            <div class="button-section">
                <div class="button-row">
                    <div class="left-text">${personnel.name}</div>
                    <div class="learn-more" onclick="toggleText(this)">En savoir +</div>
                    <a href=" ${personnel.doctolib}" target="_blank">
                        <button class="book-appointment">Prendre rendez-vous</button>
                    </a>
                </div>
                <div class="${collapsibleContentClass}">
                    <div class="content-wrapper">
                        <img src="../../../ajoutprofession/${encodeURIComponent(professionData.profession)}/${personnel.image}" alt="Profile Image" />
                        <div class="text-content">
                            ${textsHTML}
                            ${pdf}
                        </div>
                    </div>
                </div>
            </div>
        `;

        console.log("HTML injecté pour le personnel :", personnelHTML);
        personnelContainer.innerHTML += personnelHTML;
    });
}

// Fonction pour afficher/masquer le texte
function toggleText(element) {
    const content = element.parentElement.nextElementSibling;
    content.classList.toggle('show');
}
