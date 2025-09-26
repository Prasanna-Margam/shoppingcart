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