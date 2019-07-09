// get button to open Modal 
var openModalBtn = document.getElementById('openModalBtn');
// get button to close Modal
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