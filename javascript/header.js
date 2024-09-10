document.addEventListener("DOMContentLoaded", function() {
    fetch('/html/header.html')
        .then(response => response.text())
        .then(data => {
            document.querySelector('#main-header').innerHTML = data;

            // Ajouter la classe active au lien de navigation correspondant
            const path = window.location.pathname;

            const navLinks = document.querySelectorAll('nav a');
            navLinks.forEach(link => {
                if (link.getAttribute('href') === path) {
                    link.classList.add('active');
                }
            });

            // Charger dynamiquement les professions générales et spécifiques
            fetch('/json/professions.json')
                .then(response => response.json())
                .then(professions => {
                    const generalProfessionsContainer = document.getElementById('para-medical');
                    const specificProfessionsContainer = document.getElementById('specific-professions');

                    professions.forEach(prof => {
                        const professionName = prof.profession;
                        const li = document.createElement('li');
                        const a = document.createElement('a');
                        a.href = `/ajoutprofession/modele.html?profession=${professionName}`;
                        a.textContent = professionName.charAt(0).toUpperCase() + professionName.slice(1);
                        li.appendChild(a);

                        // Déterminer si la profession est générale ou spécifique
                        if (prof.type === 'general') {
                            generalProfessionsContainer.appendChild(li);
                        } else if (prof.type === 'specific') {
                            specificProfessionsContainer.appendChild(li);
                        }

                        // Ajouter la classe active si la profession correspond à l'URL
                        if (window.location.search.includes(`profession=${professionName}`)) {
                            a.classList.add('active');
                        }
                    });
                })
                .catch(error => console.error('Error loading professions:', error));
        })
        .catch(error => console.error('Error loading header:', error));
});
