let addBtn = document.getElementById('a_btn')
let tasks = document.getElementById('tasks-list')

addBtn.addEventListener('click', function(){
    if(document.getElementById('input').value === ''){
        alert('Enter a task')
    }
    else{
        tasks.innerHTML += `<div class='task'>
        <p id='para'>${document.getElementById('input').value}</p>
        <button class="t-btn">X</button>
        </div>`
        document.getElementById('input').value = ''
    }

})

tasks.addEventListener('click', function(event) {
    if (event.target.classList.contains('t-btn')) {
        event.target.parentNode.remove();
    }
})