document.addEventListener("DOMContentLoaded", function() {
    // Récupérer le nom de la profession à partir de l'URL
    const path = window.location.pathname.split('/');
    const profession = path[path.length - 2]; // Le nom du dossier de la profession

    // Mettre à jour le logo et le titre de la profession
    const professionLogo = document.getElementById('profession-logo');
    const professionTitle = document.getElementById('profession-title');

    professionLogo.src = `/ajoutprofession/${profession}/logo-${profession}.png`;
    professionLogo.alt = `Logo ${profession.charAt(0).toUpperCase() + profession.slice(1)}`;
    professionTitle.textContent = profession.charAt(0).toUpperCase() + profession.slice(1);
});
