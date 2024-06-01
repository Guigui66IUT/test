document.addEventListener('DOMContentLoaded', () => {
    fetch('../../../medecins_content.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById('medecins-container');
            data.forEach(medecin => {
                const pdf = medecin.pdf ? `<a href="../../../${medecin.pdf.path}" download="${medecin.pdf.name}" class="download-link">Autre</a>` : '';
                const textsHTML = medecin.texts.map(text => `
                    <h4>${text.filename}</h4>
                    <ul>
                        ${text.content.map(line => `<li>• ${line}</li>`).join('')}
                    </ul>
                `).join('');

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
                                <img src="../../../${medecin.image}" alt="Profile Image" />
                                <div class="text-content">
                                    ${textsHTML}
                                    ${pdf}
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
