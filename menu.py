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
#list the products
def list_products():
    print("Available Products:")
    print( "{:<5} {:<15} {:<10}".format("pid", "Product", "Price (₹)")
)
    print("-"*35)
    for pid, details in products.items():
        print(f"{pid :<5} {details['name']:<15} - ${details['price']:<10}")
    print("-"*35)
list_products()
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
#view cart items        
def view_cart():
    if not cart:
        print(" Your cart is empty.")
        return

    print(" Your Shopping Cart:")
    total = 0
    for pid, qty in cart.items():
        product = products[pid]
        subtotal = product['price'] * qty
        total += subtotal
        print(f" {product['name']} x{qty} = ${subtotal:}")
    print(f" Total: ${total:}")
view_cart()
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
#remove from the cart
def remove_from_cart(product_id):
    if product_id in cart:
        name = products[product_id]['name']
        del cart[product_id]
        print(f" Removed {name} from your cart.")
    else:
        print("product not in cart.")
remove_from_cart(1)
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

def menu():
    while True:
        print("\n===== Shopping Cart =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            list_products()
        elif choice == "2":
            try:
                pid = int(input("Enter Product ID to add: "))
                qty = int(input("Enter Quantity: "))
                add_to_cart(pid, qty)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "3":
            view_cart()
        elif choice == "4":
            try:
                pid = int(input("Enter Product ID to update: "))
                qty = int(input("Enter new Quantity: "))
                update_cart(pid, qty)
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif choice == "5":
             try:
                pid = int(input("Enter Product ID to remove: "))
                remove_from_cart(pid)
             except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "6":
            checkout()
        elif choice == "7":
            print(" Exiting... Thank you for visiting!")
            break
        else:
            print("Invalid choice, please try again.")

menu()
