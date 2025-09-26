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
#updating the cart 
def update_cart(product_id, new_quantity):
    if product_id not in cart:
        print("product not in cart.")
        return

    if new_quantity <= 0:
        del cart[product_id]
        print(f" Removed {products[product_id]['name']} from your cart.\n")
    else:
        cart[product_id] = new_quantity
        print(f" Updated {products[product_id]['name']} quantity to {new_quantity}.\n")
update_cart(1,3)