// =====================
// SMOOTH SCROLL
// =====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// =====================
// NAVBAR SCROLL EFFECT
// =====================
const nav = document.querySelector('nav');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        nav.style.boxShadow = '0 4px 20px rgba(0,0,0,0.1)';
        nav.style.background = 'rgba(250, 248, 245, 0.98)';
    } else {
        nav.style.boxShadow = 'none';
        nav.style.background = 'rgba(250, 248, 245, 0.95)';
    }
});

// =====================
// ACTIVE NAV LINK
// =====================
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav__links a');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        if (window.scrollY >= sectionTop) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.style.color = '';
        if (link.getAttribute('href') === `#${current}`) {
            link.style.color = '#1a1a1a';
        }
    });
});

// =====================
// SCROLL ANIMATIONS
// =====================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Apply animation to these elements
const animateElements = document.querySelectorAll(
    '.project-card, .skill-cat, .about__stats > div, .stat__number'
);

animateElements.forEach((el, index) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
    observer.observe(el);
});

// =====================
// COUNTER ANIMATION
// =====================
const counters = document.querySelectorAll('.stat__number');

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const target = entry.target;
            const text = target.textContent;
            const number = parseInt(text);

            if (!isNaN(number)) {
                let current = 0;
                const increment = number / 40;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= number) {
                        target.textContent = text; // restore original with +/year
                        clearInterval(timer);
                    } else {
                        target.textContent = Math.floor(current) + (text.includes('+') ? '+' : '');
                    }
                }, 40);
            }
            counterObserver.unobserve(target);
        }
    });
}, { threshold: 0.5 });

counters.forEach(counter => counterObserver.observe(counter));
// =====================
// MOBILE MENU TOGGLE
// =====================
const navLinks = document.querySelector('.nav__links');

// Create hamburger button
const hamburger = document.createElement('button');
hamburger.innerHTML = '☰';
hamburger.style.cssText = `
    display: none;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #1a1a1a;
`;

nav.appendChild(hamburger);

hamburger.addEventListener('click', () => {
    const isOpen = navLinks.style.display === 'flex';
    navLinks.style.display = isOpen ? 'none' : 'flex';
    navLinks.style.flexDirection = 'column';
    navLinks.style.position = 'absolute';
    navLinks.style.top = '60px';
    navLinks.style.right = '30px';
    navLinks.style.background = 'white';
    navLinks.style.padding = '20px';
    navLinks.style.borderRadius = '8px';
    navLinks.style.boxShadow = '0 10px 30px rgba(0,0,0,0.1)';
    hamburger.innerHTML = isOpen ? '☰' : '✕';
});

// Show/hide hamburger based on screen size
const checkScreen = () => {
    if (window.innerWidth <= 600) {
        hamburger.style.display = 'block';
        navLinks.style.display = 'none';
    } else {
        hamburger.style.display = 'none';
        navLinks.style.display = 'flex';
        navLinks.style.flexDirection = 'row';
        navLinks.style.position = 'static';
        navLinks.style.background = 'none';
        navLinks.style.padding = '0';
        navLinks.style.boxShadow = 'none';
    }
};

window.addEventListener('resize', checkScreen);
checkScreen();

// =====================
// TYPING EFFECT (HERO)
// =====================
const heroTitle = document.querySelector('.hero__title');

if (heroTitle) {
    const words = ['Student', 'Developer', 'Analyst', 'Machine Learning'];
    let wordIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    const em = heroTitle.querySelector('em');
    if (em) {
        const type = () => {
            const currentWord = words[wordIndex];

            if (isDeleting) {
                em.textContent = currentWord.substring(0, charIndex - 1);
                charIndex--;
            } else {
                em.textContent = currentWord.substring(0, charIndex + 1);
                charIndex++;
            }

            if (!isDeleting && charIndex === currentWord.length) {
                setTimeout(() => { isDeleting = true; }, 2000);
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
            }

            setTimeout(type, isDeleting ? 60 : 100);
        };

        setTimeout(type, 1500);
    }
}


// =====================
// MOBILE MENU TOGGLE
// =====================
const navLinks = document.querySelector('.nav__links');
const hamburger = document.getElementById('hamburger');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        const isOpen = navLinks.classList.contains('open');
        navLinks.classList.toggle('open');
        hamburger.innerHTML = isOpen ? '☰' : '✕';
    });

    // Close menu when a link is clicked
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('open');
            hamburger.innerHTML = '☰';
        });
    });
}