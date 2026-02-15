// Heartroot — Katie Tudor
document.addEventListener('DOMContentLoaded', () => {

    // Mobile nav toggle
    const toggle = document.querySelector('.nav-toggle');
    const navList = document.querySelector('nav ul');

    if (toggle && navList) {
        toggle.addEventListener('click', () => {
            navList.classList.toggle('active');
        });

        // Close menu when a link is clicked
        navList.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navList.classList.remove('active');
            });
        });
    }

    // Fade-in sections on scroll
    const sections = document.querySelectorAll('section');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        observer.observe(section);
    });
});

// Helper: make sections visible
document.addEventListener('DOMContentLoaded', () => {
    const style = document.createElement('style');
    style.textContent = 'section.visible { opacity: 1 !important; transform: translateY(0) !important; }';
    document.head.appendChild(style);
});
