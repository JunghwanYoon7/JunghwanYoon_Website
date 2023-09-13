const section = document.querySelectorAll('.section');
const sectBtns = document.querySelectorAll('.controlls');
const sectBtn = document.querySelectorAll('.control');
const allSections = document.querySelectorAll('.main-content');

function PageTransitions(){
    for(let i = 0; i < sectBtn.length; i++){
        sectBtn[i].addEventListener('click', function(){
            let currentBtn = document.querySelectorAll('.active-btn');
            currentBtn[0].className= currentBtn[0].className.replace('active-btn', '');
            this.className += 'active-btn'
        })
    }

//     //section active class
//     allSections.addEventListener('click', (e) => {
//         const id = e.target.dataset.id;

//         if(id){
//             //remove selected from other button
//             sectBtns.forEach((btn) =>{
//                 btn.classList.remove('active-btn')
//             })

//             e.target.classList.add('active-btn')

//             sections.forEach((section) =>{
//                 section.classList.remove('active-btn')
//             })

//             const element = document.getElementById(id);
//             element.classList.add('active-btn');
//         }
//     })
}

PageTransitions();
