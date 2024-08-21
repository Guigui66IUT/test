document.addEventListener('DOMContentLoaded', function() {
	// Charger les images dynamiquement
	const sliders = document.querySelectorAll('.slider-container');

	sliders.forEach(slider => {
		const imageContainer = slider.querySelector('.image-container');
		const dataImgPath = slider.getAttribute('data-img-path');
		const dataPageName = slider.getAttribute('data-page-name') || 'index';
		const jsonFile = `../../json/${dataPageName}_images.json`;

		// Charger le fichier JSON et ajouter les images
		fetch(jsonFile)
			.then(response => response.json())
			.then(images => {
				images.forEach(image => {
					const imgElement = document.createElement('img');
					imgElement.src = `${dataImgPath}${image}`;
					imgElement.alt = image;
					imageContainer.appendChild(imgElement);
				});

				// Initialiser le carrousel après que les images ont été ajoutées
				initializeCarousel(slider);
			})
			.catch(error => console.error('Erreur de chargement des images:', error));
	});

	// Fonction pour initialiser le carrousel
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

	// Ajuster la hauteur des cartes (si nécessaire)
	const wrapperHeight = document.querySelector('.wrapper').offsetHeight;
	const cards = document.querySelectorAll('.card');
	cards.forEach(function(card) {
		card.style.height = wrapperHeight + 'px';
	});
});

// Fonction pour afficher/masquer le texte
function toggleText(element) {
	var content = element.parentElement.nextElementSibling;
	if (content.style.display === "none" || content.style.display === "") {
		content.style.display = "block";
	} else {
		content.style.display = "none";
	}
}
