document.addEventListener('DOMContentLoaded', () => {
    fetch('../../../json/traitementkine_content.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("Data loaded:", data);
            const container = document.querySelector('.grid');
            data.forEach(medecin => {
                const medecinHTML = `
                    <div class="card">
                        <div class="img-box">
                            <img src="../../../kinesitherapeutes/traitement/${medecin.image}" alt="${medecin.name}">
                        </div>
                        <div class="card-content">
                            <h1 class="card-heading">${medecin.name}</h1>
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
