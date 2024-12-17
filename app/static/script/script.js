document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.update-cart').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const url = this.getAttribute('data-url');
            const itemId = this.getAttribute('data-item-id');

            fetch(url, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const row = document.querySelector(`[data-item-row="${data.item_id}"]`);
                    if (row) {
                        if (data.new_quantity > 0) {
                            row.querySelector('.item-quantity').textContent = data.new_quantity;
                            row.querySelector('.item-subtotal').textContent = '£' + data.item_subtotal.toFixed(2);
                        } else {
                            // Remove the row if quantity is not more than zero
                            row.remove();
                        }
                    }
                    // Update total price
                    const totalPriceElement = document.querySelector('#total-price');
                    if (totalPriceElement) {
                        totalPriceElement.textContent = '£' + data.total_price.toFixed(2);
                    }
                    // Update cart count in navbar
                    const cartCountElement = document.querySelector('#cart-count');
                    if (cartCountElement && data.total_quantity !== undefined) {
                        cartCountElement.textContent = data.total_quantity;
                    }
                    // If total_quantity is now 0, the cart is empty
                    if (data.total_quantity === 0) {
                        location.reload();
                    }

                } else {
                    alert('An error occurred. Please try again.');
                }
            })
            .catch(err => console.error('Error:', err));
        });
    });
});