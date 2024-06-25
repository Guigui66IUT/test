document.addEventListener("DOMContentLoaded", function() {
    const path = window.location.pathname.split('/');
    const profession = path[path.length - 2]; // Le nom du dossier de la profession

    const professionLogo = document.getElementById('profession-logo');
    const professionTitle = document.getElementById('profession-title');

    professionLogo.src = `/ajoutprofession/${profession}/logo-${profession}.png`;
    professionLogo.alt = `Logo ${profession.charAt(0).toUpperCase() + profession.slice(1)}`;
    professionTitle.textContent = profession.charAt(0).toUpperCase() + profession.slice(1);
});
