function toggleText(element) {
    const collapsibleContent = element.parentElement.nextElementSibling;
    collapsibleContent.style.display = (collapsibleContent.style.display === 'none' || collapsibleContent.style.display === '') ? 'block' : 'none';
}
