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










