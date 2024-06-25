document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const profession = urlParams.get('profession');

    if (profession) {
        const professionLogo = document.getElementById('profession-logo');
        const professionTitle = document.getElementById('profession-title');

        professionLogo.src = `/ajoutprofession/${profession}/logo-${profession}.png`;
        professionLogo.alt = `Logo ${profession.charAt(0).toUpperCase() + profession.slice(1)}`;
        professionTitle.textContent = profession.charAt(0).toUpperCase() + profession.slice(1);
    }
});
