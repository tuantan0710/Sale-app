def cart_stats(cart):
    total_quantity = 0
    total_amount = 0
    if cart:
        for c in cart.values():
            quantity = c.get('quantity', 0)
            price = c.get('price', 0)
            total_quantity += c['quantity']
            total_amount += c['quantity']*c['price']

    return {
        "total_quantity": total_quantity,
        "total_amount": total_amount
    }