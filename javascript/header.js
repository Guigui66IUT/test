document.addEventListener("DOMContentLoaded", function() {
    fetch('/html/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header').innerHTML = data;
            adjustPaths();
        });

    function adjustPaths() {
        const header = document.getElementById('header');
        const links = header.querySelectorAll('a');
        const depth = window.location.pathname.split('/').length - 3;

        links.forEach(link => {
            if (link.getAttribute('href').startsWith('/')) {
                let path = link.getAttribute('href').substring(1);
                for (let i = 0; i < depth; i++) {
                    path = '../' + path;
                }
                link.setAttribute('href', path);
            }
        });
    }
});
