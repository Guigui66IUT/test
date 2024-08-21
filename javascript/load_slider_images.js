document.addEventListener('DOMContentLoaded', () => {
    const sliderContainer = document.querySelector('.slider-container');
    const pageName = sliderContainer.getAttribute('data-page-name') || 'index';
    const jsonFile = `../../json/${pageName}_images.json`;

    fetch(jsonFile)
        .then(response => response.json())
        .then(images => {
            const imageContainer = document.getElementById('image-container');
            
            images.forEach(image => {
                const img = document.createElement('img');
                img.src = `${sliderContainer.getAttribute('data-img-path')}${image}`;
                img.alt = image;
                imageContainer.appendChild(img);
            });
        })
        .catch(error => console.error('Error loading images:', error));
});
