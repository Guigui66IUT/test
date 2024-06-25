document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const profession = urlParams.get('profession');

    if (profession) {
        const professionLogo = document.getElementById('profession-logo');
        const professionTitle = document.getElementById('profession-title');

        // Chemin du logo
        const logoPath = `/ajoutprofession/${profession}/logo-${profession}.png`;

        // Vérifier l'existence du logo
        fetch(logoPath)
            .then(response => {
                if (response.ok) {
                    professionLogo.src = logoPath;
                    professionLogo.alt = `Logo ${profession.charAt(0).toUpperCase() + profession.slice(1)}`;
                    professionLogo.style.display = 'block';
                } else {
                    professionLogo.style.display = 'none';
                }
            })
            .catch(() => {
                professionLogo.style.display = 'none';
            });

        professionTitle.textContent = profession.charAt(0).toUpperCase() + profession.slice(1);
    }
});
