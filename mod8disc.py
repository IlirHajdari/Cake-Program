class Cake():
    def __init__(self, cake_flavor, icing_flavor, diameter, price):
        self.cake_flavor = cake_flavor
        self.icing_flavor = icing_flavor
        self.diameter = diameter
        self.price = price
        
customer_cake = Cake("vanilla", "chocolate", 12, 10)


print(customer_cake.cake_flavor)
print(customer_cake.icing_flavor)
print(customer_cake.diameter)
print(customer_cake.price)