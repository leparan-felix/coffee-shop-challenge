import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order.all.clear()
        self.alice = Customer("Alice")
        self.bob = Customer("Bob")
        self.latte = Coffee("Latte")
        self.order1 = self.alice.create_order(self.latte, 5.0)
        self.order2 = self.bob.create_order(self.latte, 7.0)

    def test_valid_name(self):
        self.assertEqual(self.latte.name, "Latte")

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError):
            Coffee("Hi")

    def test_orders(self):
        self.assertEqual(len(self.latte.orders()), 2)

    def test_customers(self):
        customers = self.latte.customers()
        self.assertIn(self.alice, customers)
        self.assertIn(self.bob, customers)

    def test_num_orders(self):
        self.assertEqual(self.latte.num_orders(), 2)

    def test_average_price(self):
        self.assertEqual(self.latte.average_price(), 6.0)

if __name__ == '__main__':
    unittest.main()
