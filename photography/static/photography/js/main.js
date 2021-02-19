const navSlide = () => {
    const header = document.querySelector('.header');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    header.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
    

    navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 1s ease forwards ${index / 7 + 0.5}s`;
            }
        });
         header.classList.toggle('toggle');
    });

}

navSlide();