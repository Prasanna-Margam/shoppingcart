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
#remove from the cart
def remove_from_cart(product_id):
    if product_id in cart:
        name = products[product_id]['name']
        del cart[product_id]
        print(f" Removed {name} from your cart.")
    else:
        print("product not in cart.")
remove_from_cart(1)