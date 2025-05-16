import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all.clear()
        self.alice = Customer("Alice")
        self.latte = Coffee("Latte")
        self.order = Order(self.alice, self.latte, 5.0)

    def test_order_properties(self):
        self.assertEqual(self.order.customer, self.alice)
        self.assertEqual(self.order.coffee, self.latte)
        self.assertEqual(self.order.price, 5.0)

    def test_price_validation(self):
        with self.assertRaises(ValueError):
            Order(self.alice, self.latte, 0.5)

    def test_type_enforcement(self):
        with self.assertRaises(TypeError):
            Order("notacustomer", self.latte, 5.0)

if __name__ == '__main__':
    unittest.main()
