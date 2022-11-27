console.log('All system go!')

// Get Stripe publishable key
fetch("/checkout/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  console.log(stripe)
});
