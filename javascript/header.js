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

            if (window.location.pathname.startsWith('/html/profession/') || window.location.pathname.startsWith('/ajout_para-med/')) {
                const professionalDropdown = document.querySelector('.dropdown > a');
                professionalDropdown.classList.add('active');
            }

            // Charger dynamiquement les professions générales et spécifiques
            fetch('/json/professions.json')
                .then(response => response.json())
                .then(professions => {
                    const generalProfessionsContainer = document.getElementById('para-medical'); // Conteneur pour les professions générales
                    const specificProfessionsContainer = document.getElementById('specific-professions'); // Conteneur pour les professions spécifiques

                    professions.forEach(prof => {
                        const professionName = prof.profession;
                        const li = document.createElement('li');
                        const a = document.createElement('a');
                        a.href = `/ajoutprofession/modele.html?profession=${professionName}`;
                        a.textContent = professionName.charAt(0).toUpperCase() + professionName.slice(1);
                        li.appendChild(a);

                        // Si la profession est de type 'general', ajouter au conteneur général
                        if (prof.type === 'general') {
                            generalProfessionsContainer.appendChild(li);
                        } 
                        // Si la profession est de type 'specific', ajouter au conteneur spécifique
                        else if (prof.type === 'specific') {
                            specificProfessionsContainer.appendChild(li);
                        }

                        if (window.location.search.includes(`profession=${professionName}`)) {
                            a.classList.add('active');
                        }
                    });
                })
                .catch(error => console.error('Error loading professions:', error));
        })
        .catch(error => console.error('Error loading header:', error));
});
