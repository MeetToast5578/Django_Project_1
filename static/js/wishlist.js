let updateWishList = document.getElementsByClassName('add-to-wishlist')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftokenWish = getCookie('csrftoken');

for (let i = 0; i < updateWishList.length; i++) {
    updateWishList[i].addEventListener('click', function (event) {
        event.preventDefault()
        productId = this.dataset.product
        action = this.dataset.action

        console.log('Item added!', productId, action)

        let url = '/en/account/update-item/'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftokenWish
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action
            })
        }).then((response) => {
            return response.json()
        }).then((data) => {
            console.log(data)
            location.reload()
        })

    })
}