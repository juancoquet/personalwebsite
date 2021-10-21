const contact = document.querySelector('.nav__contact');
const modalAll = document.querySelector('.modal-overlay');
const modalClose = document.querySelector('.modal__close');
const codeTab = document.querySelector('#code-tab');
const codeTabItems = document.querySelectorAll('.code-tab');
const musicTab = document.querySelector('#music-tab');
const musicTabItems = document.querySelectorAll('.music-tab');



contact.addEventListener('click', openModal);

function openModal() {
    modalAll.classList.remove('hidden');
}


modalClose.addEventListener('click', closeModal);

function closeModal() {
    modalAll.classList.add('hidden');
}


codeTab.addEventListener('click', setCodeTheme);

function setCodeTheme() {
    document.body.classList.remove("music-theme");
    document.body.classList.add("code-theme");
    musicTabItems.forEach(item => {
        item.classList.add('hidden');
    })
    codeTabItems.forEach(item => {
        item.classList.remove('hidden');
    })
}

musicTab.addEventListener('click', setMusicTheme);

function setMusicTheme() {
    document.body.classList.remove("code-theme");
    document.body.classList.add("music-theme");
    codeTabItems.forEach(item => {
        item.classList.add('hidden');
    })
    musicTabItems.forEach(item => {
        item.classList.remove('hidden');
    })
}