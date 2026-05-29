class Product:
    def __init__(self, name, price, product_id, stock):
        if not product_id:
            raise ValueError("Product ID cannot be empty")
        if not name:
            raise ValueError("Product name cannot be empty")
        if price is None or price == "":
            raise ValueError("Price is required")
        if stock is None or stock == "":
            raise ValueError("Stock is required")
        if float(price) < 0:
            raise ValueError("Price cannot be negative")
        if int(stock) < 0:
            raise ValueError("Stock cannot be negative")
        self.name = name
        self.price = float(price)
        self.product_id = product_id
        self.stock = int(stock)

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_line_total(self):
        return self.product.price * self.quantity

class Cart:
    def __init__(self):
        self.items = {}
        
    def add_product(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id].quantity += quantity
        else:
            self.items[product.product_id] = CartItem(product, quantity)

    def view_cart(self):
        cart_contents = []
        for item in self.items.values():
            cart_contents.append({
                'product_name': item.product.name,
                'quantity': item.quantity,
                'line_total': item.calculate_line_total()
            })
        return cart_contents
    
    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item.calculate_line_total()
        return total
    
    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
        else:
            print(f"Product with ID {product_id} not found in cart.")

    def update_quantity(self, product_id, quantity):
        if product_id in self.items:
            self.items[product_id].quantity = quantity
        else:
            print(f"Product with ID {product_id} not found in cart.")