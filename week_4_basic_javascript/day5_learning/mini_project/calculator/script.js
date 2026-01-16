let btn = document.querySelector('.op-btn')
let inp_area = document.getElementById('para')
const s_char = ["%", "*", "/", "-", "+", "="]
let output = ''

btn.addEventListener('click', function(){
    if (event.target.tagName === "BUTTON"){
        if (event.target.textContent === 'AC'){
             output = ''
             inp_area.textContent = '0'
        }
        else if (event.target.textContent === 'DEL'){
             output = output.toString().slice(0, -1);
             if(output.length === 0){
                 inp_area.textContent = '0'
             }
             else{
                 inp_area.textContent = output
             }
        }
        else if (output === "" && s_char.includes(event.target.textContent)){
            inp_area.textContent = '0'
        }
        else if (event.target.textContent === '='){
            output = eval(output)
            inp_area.textContent = output
        }
        else{
             const lastChar = output.toString().slice(-1);
             if (s_char.includes(event.target.textContent) && s_char.includes(lastChar)){
                 return;
             }
             output = output + event.target.textContent
             inp_area.textContent = output
        }
    }
})