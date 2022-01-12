const stampOpenBtns = document.getElementsByClassName('picturebook__modal-open');
const stampCloseBtns = document.getElementsByClassName('picturebook__modal-close');
const stampModal = document.getElementsByClassName('picturebook__modal');
// const bg = document.getElementsByClassName('main__bg');
// const title = document.getElementsByClassName('picturebook__ttl');
// const picturebook = document.getElementsByClassName('picturebook__stamps');
// const stamps = document.getElementsByClassName('picturebook__stamp');
// const btn = document.getElementsByClassName('picturebook__btn');
const detailModal = document.getElementsByClassName('picturebook__modal-detail');
const detailOpenBtns = document.getElementsByClassName('picturebook__todetail-btn');
const detailCloseBtns = document.getElementsByClassName('modal__detail-close');

for (let i = 0; i < detailOpenBtns.length; i++) {
    console.log(detailOpenBtns[i]);
    console.log(detailModal[i]);
    detailOpenBtns[i].addEventListener('click', {
        value: i,
        handleEvent: detailOpen
    });

    stampCloseBtns[i].addEventListener('click', {
        value: i,
        handleEvent: detailClose
    });
}

function detailOpen() {
    detailModal[this.value].style.display = 'block';
}

function detailClose() {
    detailModal[this.value].style.display = 'none';
}