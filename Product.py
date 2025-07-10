class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def print_name(self):
            return self.name
    def print_price(self):
            return self.price
s1=Product("ram",5)
print(s1.print_name())
print(s1.print_price())