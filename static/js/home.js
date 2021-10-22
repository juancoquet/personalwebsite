const contact = document.querySelector('.nav__contact');
const modalAll = document.querySelector('.modal-overlay');
const modalClose = document.querySelector('.modal__close');
const modalCard = document.querySelector('.modal');
const codeTab = document.querySelector('#code-tab');
const codeTabItems = document.querySelectorAll('.code-tab');
const musicTab = document.querySelector('#music-tab');
const musicTabItems = document.querySelectorAll('.music-tab');



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


// Code/Music --------------------------------------

codeTab.addEventListener('click', setCodeTheme);

async function setCodeTheme() {
    document.body.classList.remove("music-theme");
    document.body.classList.add("code-theme");
    musicTab.classList.remove('tab--selected');
    codeTab.classList.add('tab--selected');

    musicTabItems.forEach(item => {
        item.classList.remove('enter');
        item.classList.add('leave-right');
    })
    await sleep(0.5);
    musicTabItems.forEach(item => {
        item.classList.add('hidden');
    })

    codeTabItems.forEach(item => {
        item.classList.remove('hidden');
    })
    await sleep(0.05);
    codeTabItems.forEach(item => {
        item.classList.add('enter');
        item.classList.remove('leave-left');
    })
}

musicTab.addEventListener('click', setMusicTheme);

async function setMusicTheme() {
    document.body.classList.remove("code-theme");
    document.body.classList.add("music-theme");
    codeTab.classList.remove('tab--selected');
    musicTab.classList.add('tab--selected');

    codeTabItems.forEach(item => {
        item.classList.remove('enter');
        item.classList.add('leave-left');
    })
    await sleep(0.5);
    codeTabItems.forEach(item => {
        item.classList.add('hidden');
    })

    musicTabItems.forEach(item => {
        item.classList.remove('hidden');
    })
    await sleep(0.05);
    musicTabItems.forEach(item => {
        item.classList.add('enter');
        item.classList.remove('leave-right');
    })
}


// Fade on load -------------------------------------

const jc = document.querySelector('#hero-name');
const caption = document.querySelector('#hero-caption');
const codeElements = document.querySelectorAll('.code-tab>*');

document.addEventListener('DOMContentLoaded', fadeInHeroText);
document.addEventListener('DOMContentLoaded', removeAnimations);

async function fadeInHeroText() {
    await sleep(0.5);
    jc.classList.replace('leave-left--hero', 'enter--load');
    caption.classList.replace('leave-right--hero', 'enter--load');
}

async function removeAnimations() {
    await sleep(2);
    codeElements.forEach(el => {
        el.style.animation = 'none';
    })
}



// Utility ----------------------------------

function sleep(s) {
    let ms = s * 1000;
    return new Promise(resolve => setTimeout(resolve, ms));
    // call await sleep(s); inside an async fucntion to use.
}