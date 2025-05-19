from customer import Customer
from coffee import Coffee
from order import Order

# Sample setup
alice = Customer("Alice")
bob = Customer("Bob")
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Create some orders
alice.create_order(latte, 5.0)
alice.create_order(mocha, 6.0)
bob.create_order(latte, 7.5)

# Debug prints
print("Alice's Coffees:", [c.name for c in alice.coffees()])
print("Latte Customers:", [c.name for c in latte.customers()])
print("Latte Average Price:", latte.average_price())
print("Top Spender on Latte:", Customer.most_aficionado(latte).name)
print("Bob's Orders:", [(o.coffee.name, o.price) for o in bob.orders()])
print("Alice's Orders:", [(o.coffee.name, o.price) for o in alice.orders()])
print("Total Orders for Latte:", latte.num_orders())
print("Total Orders for Mocha:", mocha.num_orders())
print("Total Orders for Alice:", len(alice.orders()))
print("Total Orders for Bob:", len(bob.orders()))
