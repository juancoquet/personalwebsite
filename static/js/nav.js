const contact = document.querySelector('.nav__contact');


// Modal --------------------------------------------

contact.addEventListener('click', openModal);

async function openModal() {
    modalAll.classList.remove('hidden');
    await sleep(0.05);
    modalAll.classList.add('enter');
    modalCard.classList.replace('leave-top', 'enter');

}


modalClose.addEventListener('click', closeModal);

async function closeModal() {
    modalCard.classList.replace('enter', 'leave-top');
    modalAll.classList.remove('enter');
    await sleep(0.5);
    modalAll.classList.add('hidden');
}


// Mobile Menu --------------------------------------------

const menuBtn = document.querySelector('.nav__menu');
const menuClose = document.querySelector('.nav__menu-close');
const navItems = document.querySelectorAll('.nav__item');
const menu = document.querySelector('.mobile-menu');
const navRight = document.querySelector('.nav-items--right');

menuBtn.addEventListener('click', openMenu);
menuClose.addEventListener('click', closeMenu);

async function openMenu() {
    menuBtn.classList.toggle('hidden');
    menuClose.classList.toggle('hidden');

    navItems.forEach(item => {
        menu.appendChild(item);
        item.style.display = 'block';
    });

    menu.classList.replace('leave-top--scale', 'enter--scale');

}

async function closeMenu() {
    menuBtn.classList.toggle('hidden');
    menuClose.classList.toggle('hidden');
    menu.classList.replace('enter--scale', 'leave-top--scale');
    await sleep(0.25);

    navItems.forEach(item => {
        navRight.appendChild(item);
        item.style.display = 'none';   
    });
}

window.addEventListener('resize', calculateMenu);

function calculateMenu() {
    if (window.innerWidth > 485) {
        navItems.forEach(item => {
            navRight.appendChild(item);
            item.style.display = 'block';
        });
    } else {
        navItems.forEach(item => {
            menu.appendChild(item);
            item.style.display = 'none';
        });
    }
    menuClose.classList.add('hidden');
    menuBtn.classList.remove('hidden');
}