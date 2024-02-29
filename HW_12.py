class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.description} - ${self.price}"

class Buyer:
    def __init__(self, nickname, name, father_name, mobile_phone):
        self.nickname = nickname
        self.name = name
        self.father_name = father_name
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f"{self.name} {self.father_name} ({self.nickname}) - {self.mobile_phone}"

class Transaction:
    def __init__(self, buyer, products):
        self.buyer = buyer
        self.products = products

    def calculate_total(self):
        total = sum(product.price for product in self.products)
        return total

    def __str__(self):
        product_list = "\n".join(str(product) for product in self.products)
        total_value = self.calculate_total()
        return f"Transaction details:\nBuyer: {self.buyer}\nProducts:\n{product_list}\nTotal Value: ${total_value}"

# Test the classes
product1 = Product(29.99, "Smartphone", "5.5 x 2.8 x 0.3 inches")
product2 = Product(499.99, "Laptop", "13.3 x 9.1 x 0.7 inches")

buyer = Buyer("user123", "John", "Doe", "123-456-7890")

transaction = Transaction(buyer, [product1, product2])

# Display information about the transaction
print(transaction)
