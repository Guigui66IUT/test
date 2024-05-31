document.addEventListener('DOMContentLoaded', () => {
    fetch('medecins_content.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('medecins-container').innerHTML = data;
        })
        .catch(error => {
            console.error('Error loading medecins_content.html:', error);
        });
});
