document.addEventListener('DOMContentLoaded', () => {
    fetch('../../../json/podologues_content.json') // Charger le fichier JSON des podologues
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("Données des podologues chargées :", data); // Ajout de journalisation
            const container = document.getElementById('podologues-container'); // Conteneur pour afficher les podologues
            
            data.forEach((podologue, index) => {
                console.log("Traitement du podologue :", podologue); // Journalisation

                const pdf = podologue.pdf ? `<a href="../../${podologue.pdf.path}" download="${podologue.pdf.name}" class="download-link">Autre</a>` : '';
                const textsHTML = podologue.texts.map(text => `
                    <h4>${text.filename}</h4>
                    <ul>   
                        ${text.content.map(line => `<li>${line}</li>`).join('')}
                    </ul>
                `).join('');

                // Si un seul podologue est trouvé, ajouter la classe pour dérouler automatiquement
                const isSinglePodologue = data.length === 1;
                const collapsibleContentClass = isSinglePodologue ? 'collapsible-content show' : 'collapsible-content';

                const podologueHTML = `
                    <div class="button-section">
                        <div class="button-row">
                            <div class="left-text">${podologue.name}</div>
                            <div class="learn-more" onclick="toggleText(this)">En savoir +</div>
                            <a href="${podologue.doctolib}" target="_blank">
                                <button class="rendezvous">Prendre rendez-vous</button>
                            </a>
                        </div>
                        <div class="${collapsibleContentClass}">
                            <div class="content-wrapper">
                                <img src="../../../podologues/equipe/${podologue.image}" alt="Profile Image" />
                                <div class="text-content">
                                    ${textsHTML}
                                    ${pdf}
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                container.innerHTML += podologueHTML;
            });
        })
        .catch(error => {
            console.error('Erreur de chargement du fichier JSON des podologues:', error);
        });
});

// Fonction pour afficher/masquer le texte avec gestion du premier clic
function toggleText(element) {
    const content = element.parentElement.nextElementSibling;
    content.classList.toggle('show');
}
