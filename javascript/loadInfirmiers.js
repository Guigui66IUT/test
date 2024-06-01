document.addEventListener('DOMContentLoaded', () => {
    fetch('../../../infirmiers_content.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById('infirmiers-container');
            data.forEach(infirmier => {
                const infirmierHTML = `
                    <div class="button-section">
                        <div class="button-row">
                            <div class="left-text">${infirmier.name}</div>
                        </div>
                    </div>
                `;
                container.innerHTML += infirmierHTML;
            });
        })
        .catch(error => {
            console.error('Error loading infirmiers_content.json:', error);
        });
});
