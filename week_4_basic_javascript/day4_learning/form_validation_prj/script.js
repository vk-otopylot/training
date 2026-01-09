function validateForm(event){
    event.preventDefault()
    clearErrors()
    let name = document.getElementById('name').value
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value
    let confirm_password = document.getElementById('confirm-password').value

    if(name === ''){
        document.getElementById('name-error').textContent = 'Please fill the name field'
    }
    else if(name && name.length < 3){
        document.getElementById('name-error').textContent = 'Name should contain minimum 3 characters'
    }
    else if(email === ''){
        document.getElementById('email-error').textContent = 'Please fill the email field'
    }
    else if(!(email.includes('@')) || !(email.includes('.'))){
        document.getElementById('email-error').textContent = 'Email should contain @ and .'
    }
    else if(password.length < 6){
        document.getElementById('password-error').textContent = 'Password should contain minimum 6 character'
    }
    else if(password !== confirm_password){
        document.getElementById('confirm-password-error').textContent = 'Password and confirm password must be same'
    }
    else{
        document.getElementById('success-msg').textContent = 'Form submitted successfully.!!!'
        clearFields()
    }
}

function clearErrors() {
  document.getElementById('name-error').textContent = ''
  document.getElementById('email-error').textContent = ''
  document.getElementById('password-error').textContent = ''
  document.getElementById('confirm-password-error').textContent = ''
}

function clearFields(){
    document.getElementById('name').value = ''
    document.getElementById('email').value = ''
    document.getElementById('password').value = ''
    document.getElementById('confirm-password').value = ''
}

