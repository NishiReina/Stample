const openBtn = document.getElementById('modal-open');
const closeBtn = document.getElementById('modal-close');
const modal = document.getElementById('modal');

openBtn.addEventListener('click', () => {
    modal.style.display = 'block';
})

closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
})