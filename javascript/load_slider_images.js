window.onload = function() {
    const sliders = document.querySelectorAll('.slider-container');

    sliders.forEach(slider => {
        const imageContainer = slider.querySelector('.image-container');
        const dataImgPath = slider.getAttribute('data-img-path');
        const dataPageName = slider.getAttribute('data-page-name') || 'index';
        const jsonFile = `/json/${dataPageName}_images.json`;

        // Afficher la hauteur de `.wrapper` avant le chargement des images
        const initialWrapperHeight = document.querySelector('.wrapper').offsetHeight;
        console.log("Wrapper Height (before images loaded):", initialWrapperHeight);

        fetch(jsonFile)
            .then(response => response.json())
            .then(images => {
                let imagesLoaded = 0;
                images.forEach(image => {
                    const imgElement = document.createElement('img');
                    imgElement.src = `${dataImgPath}${image}`;
                    imgElement.alt = image;
                    imgElement.onload = function() {
                        imagesLoaded++;
                        if (imagesLoaded === images.length) {
                            // Toutes les images sont chargées
                            adjustCardHeight();
                        }
                    };
                    imageContainer.appendChild(imgElement);
                });

                // Initialiser le carrousel après que les images ont été ajoutées
                initializeCarousel(slider);
            })
            .catch(error => console.error('Erreur de chargement des images:', error));
    });

    function initializeCarousel(slider) {
        const prevBtn = slider.querySelector('.prev');
        const nextBtn = slider.querySelector('.next');
        const imageContainer = slider.querySelector('.image-container');
        const images = imageContainer.querySelectorAll('img');
        let currentImg = 1;
        let timeout;

        function updateImg() {
            if (currentImg > images.length) {
                currentImg = 1;
            } else if (currentImg < 1) {
                currentImg = images.length;
            }
            imageContainer.style.transform = 'translateX(-' + (currentImg - 1) * 800 + 'px)';
            timeout = setTimeout(() => {
                currentImg++;
                updateImg();
            }, 3000);
        }

        prevBtn.addEventListener('click', function() {
            clearTimeout(timeout);
            currentImg--;
            updateImg();
        });

        nextBtn.addEventListener('click', function() {
            clearTimeout(timeout);
            currentImg++;
            updateImg();
        });

        updateImg(); // Initialize the carousel
    }

    // Fonction pour ajuster la hauteur des cartes
    function adjustCardHeight() {
        const wrapperHeight = document.querySelector('.wrapper').offsetHeight;
        console.log("Wrapper Height (after images loaded):", wrapperHeight);

        const cards = document.querySelectorAll('.card');
        cards.forEach(function(card) {
            console.log("Setting card height to (after images loaded):", wrapperHeight);
            card.style.height = wrapperHeight + 'px';
        });
    }
};
