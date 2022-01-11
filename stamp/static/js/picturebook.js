// window.onload = () => {
//     const stampOpenBtns = document.getElementsByClassName('picturebook__modal-open');
//     const stampCloseBtns = document.getElementsByClassName('picturebook__modal-close');
//     const stampModal = document.getElementsByClassName('picturebook__modal');

//     console.log(stampOpenBtns);
//     console.log(stampModal);
//     for (let i = 0; i < stampOpenBtns.length; i++){
//         console.log(stampOpenBtns[i]);
//         console.log(stampModal[i]);
//         stampOpenBtns[i].addEventListener('click', 
//             {
//                 value: i,
//                 handleEvent: stampOpen                
//             }
//         );

//         stampCloseBtns[i].addEventListener('click', 
//             {
//                 value: i,
//                 handleEvent: stampClose            
//             }
//         );
//     }


//     function stampOpen(){
//         stampModal[this.value].style.display = 'block';
//     }

//     function stampClose(){
//         stampModal[this.value].style.display = 'none';
//     }

// };

const stampOpenBtns = document.getElementsByClassName('picturebook__modal-open');
const stampCloseBtns = document.getElementsByClassName('picturebook__modal-close');
const stampModal = document.getElementsByClassName('picturebook__modal');
const bg = document.getElementsByClassName('main__bg');
const title = document.getElementsByClassName('picturebook__ttl');
const picturebook = document.getElementsByClassName('picturebook__stamps');
const stamps = document.getElementsByClassName('picturebook__stamp');
const btn = document.getElementsByClassName('picturebook__btn');

console.log(stampOpenBtns);
console.log(stampModal);
for (let i = 0; i < stampOpenBtns.length; i++) {
    console.log(stampOpenBtns[i]);
    console.log(stampModal[i]);
    stampOpenBtns[i].addEventListener('click', {
        value: i,
        handleEvent: stampOpen
    });

    stampCloseBtns[i].addEventListener('click', {
        value: i,
        handleEvent: stampClose
    });
}


function stampOpen() {
    stampModal[this.value].style.display = 'block';
    bg[0].style.background = 'rgba(0, 0, 0, 0.5)';
    title[0].style.display = 'none';
    btn[0].style.display = 'none';
    picturebook[0].classList.add('modal-block');
    for (let i = 0; i < stamps.length; i++){
        stamps[i].style.display = 'none';
    }
}

function stampClose() {
    stampModal[this.value].style.display = 'none';
    bg[0].style.background = 'none';
    title[0].style.display = 'flex';
    btn[0].style.display = 'block';
    picturebook[0].classList.remove('modal-block');
    for (let i = 0; i < stamps.length; i++){
        stamps[i].style.display = 'block';
    }
}