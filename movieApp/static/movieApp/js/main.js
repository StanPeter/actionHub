// get button to open create-modal.html
var openModalBtn = document.getElementById('openModalBtn');
// get button to close create-modal.html
var closeModalBtn = document.getElementById('closeModalBtn');
// get modal element 
var modal = document.getElementById('modal-create-movie');

// open Modal event 
openModalBtn.addEventListener('click', openModal);
// close Modal event
closeModalBtn.addEventListener('click', closeModal);
// close Modal if click outside the Modal window
modal.addEventListener('click', outsideClick);

function openModal() {
    console.log('opening');
    modal.style.display = 'block';
}
function closeModal() {
    modal.style.display = 'none';
}
function outsideClick(e) {
    if(e.target == modal){
        modal.style.display = 'none';
    }
}

// js for detail-modal.html
// code written again to practise
var openDetail = document.getElementById('openDetail');
var closeDetail = document.getElementById('closeDetail');
var modalDetail = document.getElementById('modal-detail-movie');

openDetail.addEventListener('click', detailOpen);
closeDetail.addEventListener('click', detailCLose);
modalDetail.addEventListener('click', clickOutside);

function detailOpen() {
    console.log('opening detail');
    modalDetail.style.display = 'block';
}
function detailCLose() {
    modalDetail.style.display = 'none';
}
function clickOutside(e) {
    if(e.target == modalDetail){
        modalDetail.style.display = 'none';
    }
}