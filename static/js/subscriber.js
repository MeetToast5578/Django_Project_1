let subscribeForm = document.getElementById('mc-embedded-subscribe-form')

subscribeForm.addEventListener('submit', function(e){
    e.preventDefault()
    let email = document.getElementById('email').value
    console.log('test')
    fetch('http://127.0.0.1:8000/api/subscriber/', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : subscribeForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify({'email' : email})
    }).then(
        response =>{
            if (response.ok){
                subscribeForm.innerHTML = `<h2 style="color: white;" >Thanks for subscription!</h2>`
                document.getElementById('error-message').classList.add('d-none')
            }
            else{
                document.getElementById('error-message').classList.remove('d-none')

            }
        }
    )
})