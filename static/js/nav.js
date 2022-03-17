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