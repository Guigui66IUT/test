document.addEventListener('DOMContentLoaded', () => {
    // Récupérer l'attribut data-img-path qui contient le chemin des images
    const sliderContainer = document.querySelector('.slider-container');
    const imgPath = sliderContainer.getAttribute('data-img-path');

    // Charger le JSON contenant la liste des images
    fetch('json/slider_images.json')
        .then(response => response.json())
        .then(images => {
            const imageContainer = document.getElementById('image-container');
            
            images.forEach(image => {
                const img = document.createElement('img');
                img.src = `${imgPath}${image}`;
                img.alt = image;
                imageContainer.appendChild(img);
            });
        })
        .catch(error => console.error('Error loading images:', error));
});
