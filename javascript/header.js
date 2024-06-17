document.addEventListener("DOMContentLoaded", function() {
    fetch('/html/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header').innerHTML = data;
            adjustPaths();
            setActiveClass();
        });

    function adjustPaths() {
        const header = document.getElementById('header');
        const links = header.querySelectorAll('a');
        const depth = window.location.pathname.split('/').filter(part => part).length - 1;

        links.forEach(link => {
            let href = link.getAttribute('href');
            if (href.startsWith('/')) {
                href = href.substring(1);
                let path = '';
                for (let i = 0; i < depth; i++) {
                    path += '../';
                }
                path += href;
                link.setAttribute('href', path);
            }
        });
    }

    function setActiveClass() {
        const links = document.querySelectorAll('nav a');
        const currentPath = window.location.pathname;

        let activeLinkSet = false;

        links.forEach(link => {
            const linkPath = new URL(link.href).pathname;
            if (!activeLinkSet && (linkPath === currentPath || (currentPath === '/' && linkPath === '/index.html'))) {
                link.classList.add('active');
                activeLinkSet = true;
            } else {
                link.classList.remove('active');
            }
        });

        // Ajoute la classe active au lien "Professionnels de santé" si on est dans une de ses pages
        if (currentPath.includes('/html/profession/')) {
            document.querySelector('a.dropdown-toggle').classList.add('active');
        }
    }
});
