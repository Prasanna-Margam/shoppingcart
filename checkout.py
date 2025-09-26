products = {
    1: {"name": "Laptop", "price": 45000},
    2: {"name": "Smartphone", "price": 15000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Keyboard", "price": 1200},
    5: {"name": "Mouse", "price": 800},
    6: {"name": "Charger", "price": 500},
    7: {"name": "USB Cable", "price": 300},
    8: {"name": "Backpack", "price": 2500}
}

cart = {}
#checkout
def checkout():
    if not cart:
        print(" Your cart is empty! Add items before checkout.")
        return

    print("Checkout Summary:")
    total = 0
    for pid, qty in cart.items():
        product = products[pid]
        subtotal = product['price'] * qty
        total += subtotal
        print(f" {product['name']} x{qty} = ₹{subtotal}")
    print(f" Total Bill: ₹{total}")
    print(" Thank you!shop again")
    cart.clear()
checkout()