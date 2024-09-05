document.addEventListener("DOMContentLoaded", function() {
    fetch('/html/header.html')
        .then(response => response.text())
        .then(data => {
            document.querySelector('#main-header').innerHTML = data;

            // Ajouter la classe active au lien de navigation correspondant
            const path = window.location.pathname;

            // Sélectionner tous les liens de navigation
            const navLinks = document.querySelectorAll('nav a');

            navLinks.forEach(link => {
                if (link.getAttribute('href') === path) {
                    link.classList.add('active');
                }
            });

            if (window.location.pathname.startsWith('/html/profession/') || window.location.pathname.startsWith('/ajoutprofession/')) {
                const professionalDropdown = document.querySelector('.dropdown > a');
                professionalDropdown.classList.add('active');
            }

            // Charger dynamiquement les nouvelles professions
            fetch('/json/professions.json')
                .then(response => response.json())
                .then(professions => {
                    const newProfessionsContainer = document.getElementById('new-professions');
                    professions.forEach(prof => {
                        // `prof` est un objet avec une propriété `profession`
                        const professionName = prof.profession;
                        const li = document.createElement('li');
                        const a = document.createElement('a');
                        a.href = `/ajoutprofession/modele.html?profession=${professionName}`;
                        a.textContent = professionName.charAt(0).toUpperCase() + professionName.slice(1);
                        li.appendChild(a);
                        newProfessionsContainer.appendChild(li);

                        if (window.location.search.includes(`profession=${professionName}`)) {
                            a.classList.add('active');
                        }
                    });
                })
                .catch(error => console.error('Error loading new professions:', error));
        })
        .catch(error => console.error('Error loading header:', error));
});
