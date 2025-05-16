class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, object) or not isinstance(coffee, object):
            raise TypeError("Order must be associated with a Customer and a Coffee instance.")
        if not isinstance(price, (float, int)) or not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
