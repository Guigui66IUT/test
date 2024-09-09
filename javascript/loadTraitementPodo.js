document.addEventListener('DOMContentLoaded', () => {
    fetch('../../../json/traitementpodo_content.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("Data loaded:", data);
            const container = document.querySelector('.grate');
            data.forEach(traitement => {
                const traitementHTML = `
                    <div class="card">
                        <div class="img-box">
                            <img src="../../../podologues/traitement/${traitement.image}" alt="${traitement.name}">
                        </div>
                        <div class="card-content">
                            <h1 class="card-heading">${traitement.name}</h1>
                        </div>
                        <div class="text-content" style="display: none;">
                            <p>${traitement.txt}</p>
                        </div>
                    </div>
                `;
                container.innerHTML += traitementHTML;
            });

            // Add click event listeners to each card
            document.querySelectorAll('.card').forEach(card => {
                card.addEventListener('click', function() {
                    const imgBox = this.querySelector('.img-box');
                    const textContent = this.querySelector('.text-content');
                    imgBox.style.display = imgBox.style.display === 'none' ? 'block' : 'none';
                    textContent.style.display = textContent.style.display === 'none' ? 'block' : 'none';
                });
            });
        })
        .catch(error => {
            console.error('Error loading traitementpodo_content.json:', error);
        });
});
