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

            // Vérifier si la page appartient à une profession
            if (path.startsWith('/html/profession/')) {
                const professionalDropdown = document.querySelector('.dropdown > a');
                professionalDropdown.classList.add('active');
            }
        })
        .catch(error => console.error('Error loading header:', error));
});
