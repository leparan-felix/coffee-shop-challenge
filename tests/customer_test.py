import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all.clear()
        self.alice = Customer("Alice")
        self.latte = Coffee("Latte")
        self.order = self.alice.create_order(self.latte, 5.0)

    def test_valid_name(self):
        self.assertEqual(self.alice.name, "Alice")

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError):
            Customer("")

    def test_orders(self):
        self.assertIn(self.order, self.alice.orders())

    def test_coffees(self):
        self.assertIn(self.latte, self.alice.coffees())

    def test_create_order(self):
        order2 = self.alice.create_order(Coffee("Mocha"), 4.0)
        self.assertIn(order2, Order.all)

if __name__ == '__main__':
    unittest.main()
