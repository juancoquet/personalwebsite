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

function openMenu() {
    navItems.forEach(item => {
        menu.appendChild(item);
        item.style.display = 'block';   
    });
    menuBtn.classList.toggle('hidden');
    menuClose.classList.toggle('hidden');
}

function closeMenu() {
    navItems.forEach(item => {
        navRight.appendChild(item);
        item.style.display = 'none';   
    });
    menuBtn.classList.toggle('hidden');
    menuClose.classList.toggle('hidden');
}