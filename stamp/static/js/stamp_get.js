const stampModal = document.getElementsByClassName('stamp-get-modal');

const detailModal = document.getElementsByClassName('stamp-get__modal-detail');
const detailOpenBtns = document.getElementsByClassName('stamp-get__todetail-btn');
const detailCloseBtns = document.getElementsByClassName('modal__detail-close');

for (let i = 0; i < detailOpenBtns.length; i++) {
    console.log(detailOpenBtns[i]);
    console.log(detailModal[i]);
    detailOpenBtns[i].addEventListener('click', {
        value: i,
        handleEvent: detailOpen
    });

    detailCloseBtns[i].addEventListener('click', {
        value: i,
        handleEvent: detailClose
    });
}

function detailOpen() {
    detailModal[this.value].style.display = 'block';
    stampModal[0].style.display = 'none';
}

function detailClose() {
    detailModal[this.value].style.display = 'none';
    stampModal[0].style.display = 'block';
}