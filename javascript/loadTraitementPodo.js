document.addEventListener('DOMContentLoaded', () => {
    fetch('../../../json/traitementpodo_content.json')  // Modifié pour 'traitementpodo'
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("Data loaded:", data);
            const container = document.querySelector('.grid');
            data.forEach(traitement => {
                const traitementHTML = `
                    <div class="card">
                        <div class="img-box">
                            <img src="../../../traitementpodo/${traitement.image}" alt="${traitement.name}">
                        </div>
                        <div class="card-content">
                            <h1 class="card-heading">${traitement.name}</h1>
                        </div>
                    </div>
                `;
                container.innerHTML += traitementHTML;
            });
        })
        .catch(error => {
            console.error('Error loading traitementpodo_content.json:', error);
        });
});
