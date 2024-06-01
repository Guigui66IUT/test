document.addEventListener('DOMContentLoaded', () => {
    fetch('../../../medecins_content.json') // Chemin correct pour atteindre la racine du projet
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById('medecins-container');
            data.forEach(medecin => {
                const medecinHTML = `
                    <div class="button-section">
                        <div class="button-row">
                            <div class="left-text">${medecin.name}</div>
                            <div class="learn-more" onclick="toggleText(this)">En savoir +</div>
                            <a href="${medecin.doctolib}" target="_blank">
                                <button class="book-appointment">Prendre rendez-vous</button>
                            </a>
                        </div>
                        <div class="collapsible-content">
                            <div class="content-wrapper">
                                <img src="${medecin.image}" alt="Profile Image" />
                                <div class="text-content">
                                    ${medecin.texts.map(text => `<p>${text}</p>`).join('')}
                                    ${medecin.pdf ? `<a href="${medecin.pdf}" download class="download-link">Autre</a>` : ''}
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                container.innerHTML += medecinHTML;
            });
        })
        .catch(error => {
            console.error('Error loading medecins_content.json:', error);
        });
});
