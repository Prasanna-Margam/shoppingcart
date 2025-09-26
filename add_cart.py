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

#add products to cart
def add_to_cart(product_id, quantity):
    max_product=8
    if product_id not in products:
        print("Product not found")
        return

    if product_id in cart:
        cart[product_id] += quantity
    else:
         cart[product_id] = quantity
         name = products[product_id]['name']
         print(f"added {quantity} x {name} to your cart.\n")
    
    if cart[product_id]>=max_product:
        print("cannot add more products")
add_to_cart(1,2)