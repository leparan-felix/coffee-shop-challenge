📘 README.md — Coffee Shop Challenge

# ☕ Coffee Shop Challenge

A Python-based domain modeling project for a coffee shop. This challenge reinforces core Object-Oriented Programming concepts such as class design, data validation, relationships (one-to-many and many-to-many), and aggregate methods.

---

##  Project Overview

This project simulates a coffee shop ecosystem using three core models:

- **Customer**
- **Coffee**
- **Order**

### Relationships

- A **Customer** can place many **Orders**.
- A **Coffee** can appear in many **Orders**.
- An **Order** belongs to one **Customer** and one **Coffee**.

This forms a **many-to-many** relationship between **Customers** and **Coffees**, with **Order** as the join model.

---

##  Folder Structure

coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
├── customer_test.py
├── coffee_test.py
└── order_test.py


---

## Project Setup

### 1. Clone the repository

```bash
git clone git@github.com:<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge

2. Set up Python environment

Using Pipenv:

pipenv install
pipenv shell

Or alternatively, using venv:

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt  # if using pip instead of pipenv

Models & Methods
 Customer

Customer(name: str)

    Must be a string between 1–15 characters.

    .name (property) – getter/setter with validation.

    .orders() – all orders placed by the customer.

    .coffees() – unique list of coffees ordered.

    .create_order(coffee, price) – instantiate a new order.

    Customer.most_aficionado(coffee) – returns customer who spent the most on that coffee.

 Coffee

Coffee(name: str)

    Must be a string with at least 3 characters.

    .name (property) – read-only once initialized.

    .orders() – all orders for that coffee.

    .customers() – unique customers who ordered it.

    .num_orders() – total number of orders.

    .average_price() – average order price.

Order

Order(customer, coffee, price: float)

    Accepts a Customer, Coffee, and a price between 1.0–10.0.

    .customer – associated Customer.

    .coffee – associated Coffee.

    .price – read-only price.

🧪 Running the Project

Use debug.py to interact with the models manually:

python3 debug.py

To run the tests:

python3 -m unittest discover -s tests
