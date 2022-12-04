console.log('All system go!')
const form = document.getElementById('form');

// Get Stripe publishable key
fetch("/checkout/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/checkout/create-checkout-session/")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});


document.getElementById('payment-btn').addEventListener('click', function (e) {
    submitFormData();
});

function submitFormData(event) {
    var userData = {
        'name': null,
        'email': null,
        'total': total,
    }

    var shippingDetails = {
        'address': null,
        'city': null,
        'state': null,
        'zipcode': null,
        'country': null,
    }

    shippingDetails.address = form.address.value
    shippingDetails.city = form.city.value
    shippingDetails.state = form.state.value
    shippingDetails.zipcode = form.zipcode.value
    shippingDetails.country = form.country.value


    userData.name = form.name.value
    userData.email = form.email.value

    var url = "process_order/"

    fetch(url, {
            method:"POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'form': userData,
                'shipping': shippingDetails
            }),

        })
        .then((response) => response.json())
        .then((data) => {
            console.log('Success:', data);
            alert('Transaction completed');
            window.location.href = "{% url 'store' %}"
        })
}