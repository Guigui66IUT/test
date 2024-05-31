document.addEventListener("DOMContentLoaded", function() {
	const sliders = document.querySelectorAll('.slider-container');
	sliders.forEach(slider => {
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
	});
  
	const wrapperHeight = document.querySelector('.wrapper').offsetHeight;
	const cards = document.querySelectorAll('.card');
	cards.forEach(function(card) {
	  card.style.height = wrapperHeight + 'px';
	});
  });
  



function toggleText(element) {
	var content = element.parentElement.nextElementSibling;
	if (content.style.display === "none" || content.style.display === "") {
		content.style.display = "block";
	} else {
		content.style.display = "none";
	}
}











document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.pathname;
    let jsonPath = 'file_list.json';
    if (path.includes('actualite')) {
        jsonPath = '../../file_list.json';
    }

    fetch(jsonPath)
        .then(response => response.json())
        .then(files => {
            const vessel = document.getElementById('vessel');

            files.forEach(filename => {
                const card = document.createElement('div');
                card.classList.add('card');
                card.onclick = () => downloadPDF(filename);

                const img = document.createElement('img');
                img.src = `../../pdf/${filename}.jpg`; // Chemin de l'image
                img.alt = filename;

                const p = document.createElement('p');
                p.textContent = filename;

                card.appendChild(img);
                card.appendChild(p);
                vessel.appendChild(card);
            });
        });
});

function downloadPDF(filename) {
    const link = document.createElement('a');
    link.href = `../../pdf/${filename}.pdf`;
    link.download = `${filename}.pdf`;
    link.click();
}
