// スタンプモーダル
const bg = document.getElementsByClassName('route-bg');
const title = document.getElementsByClassName('route__ttl');
const picturebook = document.getElementsByClassName('picturebook__stamps');
const stamps = document.getElementsByClassName('picturebook__stamp');
const btn = document.getElementsByClassName('home__btn');
const route = document.getElementsByClassName('route__shop');
const routeNum = document.getElementsByClassName('route__detail-num');
// detailモーダル
const detailModal = document.getElementsByClassName('picturebook__modal-detail');
const detailOpenBtns = document.getElementsByClassName('route__todetail-btn');
const detailCloseBtns = document.getElementsByClassName('modal__detail-close');

// detail modal
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
    bg[0].style.background = 'rgba(0, 0, 0, 0.5)';
    title[0].style.display = 'none';
    btn[0].style.display = 'none';
    for (let i = 0; i < route.length; i++){
        route[i].style.display = 'none';
    }
    for (let i = 0; i < routeNum.length; i++){
        routeNum[i].style.display = 'none';
    }
}

function detailClose() {
    detailModal[this.value].style.display = 'none';
    bg[0].style.background = 'none';
    title[0].style.display = 'block';
    btn[0].style.display = 'block';
    for (let i = 0; i < route.length; i++){
        route[i].style.display = 'block';
    }
    for (let i = 0; i < routeNum.length; i++){
        routeNum[i].style.display = 'block';
    }
    
}