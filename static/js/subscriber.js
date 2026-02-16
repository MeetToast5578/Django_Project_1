let subscribeForm = document.getElementById('mc-embedded-subscribe-form');

subscribeForm.addEventListener('submit', function(e) {
    e.preventDefault();

    let email = document.getElementById('email').value;

    fetch('http://127.0.0.1:8000/api/subscriber/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': subscribeForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify({ 'email' : email })
    })
    .then(response => {
        if (response.ok) {
            subscribeForm.innerHTML =
                `<h2 style="color: white;">Thanks for subscription!</h2>`;
            document.getElementById('error-message').classList.add('d-none');
            return;
        }

        const errorText = document.getElementById('error-message-text');
        const errorBox = document.getElementById('error-message');

        switch (response.status) {
            case 400:
                errorText.innerText = 'Please check your input and try again.';
                break;
            case 403:
                errorText.innerText = "You don't have permission.";
                break;
            case 409:
                errorText.innerText = 'This email is already subscribed.';
                break;
            default:
                errorText.innerText = 'Something went wrong. Please try again.';
        }

        errorBox.classList.remove('d-none');
    })
    .catch(error => {
        // This handles network errors
        document.getElementById('error-message-text').innerText =
            'Unable to connect. Please check your internet.';
        document.getElementById('error-message').classList.remove('d-none');

        console.error('Network error:', error);
    });
});