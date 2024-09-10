document.addEventListener("DOMContentLoaded", function() {
    fetch('/json/professions.json')
        .then(response => response.json())
        .then(professions => {
            const newProfessionsContainer = document.getElementById('new-professions');
            professions.forEach(profession => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                a.href = `/ajoutprofession/modele.html?profession=${profession}`;
                a.textContent = profession.charAt(0).toUpperCase() + profession.slice(1);
                li.appendChild(a);
                newProfessionsContainer.insertAdjacentElement('beforebegin', li);
            });
        })
        .catch(error => console.error('Error loading new professions:', error));
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

        // Vérification des fichiers PDF et génération des liens de téléchargement
        const pdf = personnel.pdf ? `<a href="../../${personnel.pdf.path}" download="${personnel.pdf.name}" class="download-link">Autre</a>` : '';

        // Génération du HTML pour les fichiers textes
        const textsHTML = personnel.texts.map(text => `
            <h4>${text.filename}</h4>
            <ul>
                ${text.content.map(line => `<li>${line}</li>`).join('')}
            </ul>
        `).join('');

        // Si le contenu de doctolib contient un numéro de téléphone formaté, initialement afficher le bouton "Prendre rendez-vous"
        const isPhoneNumber = personnel.doctolib.match(/^\d{2} \d{2} \d{2} \d{2} \d{2}$/);
        let doctolibOrPhone = `<button class="book-appointment" onclick="revealPhoneNumber(this, '${personnel.doctolib}')">Prendre rendez-vous</button>`;

        // Si c'est un lien Doctolib, le bouton reste actif et fonctionnel
        if (!isPhoneNumber) {
            doctolibOrPhone = `<a href="${personnel.doctolib}" target="_blank">
                <button class="book-appointment">Prendre rendez-vous</button>
              </a>`;
        }

        const isSinglePersonnel = professionData.personnel.length === 1;
        const collapsibleContentClass = isSinglePersonnel ? 'collapsible-content show' : 'collapsible-content';

        const personnelHTML = `
            <div class="button-section">
                <div class="button-row">
                    <div class="left-text">${personnel.name}</div>
                    <div class="learn-more" onclick="toggleText(this)">En savoir +</div>
                    ${doctolibOrPhone}
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

// Fonction pour remplacer le bouton par le numéro de téléphone après clic
function revealPhoneNumber(button, phoneNumber) {
    button.innerText = phoneNumber;  // Remplacer le texte du bouton par le numéro de téléphone
    button.disabled = true;  // Désactiver le bouton après clic
}
