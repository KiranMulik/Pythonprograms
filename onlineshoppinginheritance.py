class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        self.items[product.name] = self.items.get(product.name, 0) + quantity
        print(f"Added {quantity} x {product.name} to the cart.")

    def remove_product(self, product_name):
        if product_name in self.items:
            del self.items[product_name]
            print(f"Removed {product_name} from the cart.")
        else:
            print(f"{product_name} is not in the cart.")
            

    def calculate_total(self, all_products):
        total = 0
        for name, quantity in self.items.items():
            for product in all_products:
                if product.name == name:
                    total += product.price * quantity
                    break
        return total

    def apply_discount(self, total, discount_percentage):
        discounted_total = total * (1 - discount_percentage / 100)
        return discounted_total

    def display_cart(self):
        print("\n--- Shopping Cart ---")
        for name, quantity in self.items.items():
            print(f"{name}: {quantity}")
        print("---------------------")

# Demo
laptop = Product("Laptop", 1200.00)
mouse = Product("Wireless Mouse", 25.00)
all_products = [laptop, mouse]

my_cart = Cart()
my_cart.add_product(laptop)
my_cart.add_product(mouse, 2)

my_cart.display_cart()

subtotal = my_cart.calculate_total(all_products)
print(f"Subtotal: ${subtotal:.2f}")

final_total = my_cart.apply_discount(subtotal, 10)
print(f"Final total after 10% discount: ${final_total:.2f}")