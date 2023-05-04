import sqlite3

full_info = """
SELECT customer.full_name, manager.full_name, purchase_amount, date
FROM 'order'
join customer
on "order".customer_id = customer.customer_id
join manager
on "order".manager_id = manager.manager_id"""

no_orders = """
SELECT full_name FROM customer WHERE customer_id NOT IN (SELECT "order".customer_id FROM 'order')"""

no_address_match = """
SELECT order_no, customer.full_name, manager.full_name
FROM "order"
join customer
on "order".customer_id = customer.customer_id
join manager
on "order".manager_id = manager.manager_id
where manager.city <> customer.city
"""

no_manager = """
SELECT order_no, customer.full_name 
from 'order'
join customer
on "order".customer_id = customer.customer_id
where "order".manager_id is null """


with sqlite3.connect("hw.db") as conn:
    c = conn.cursor()
    for item in [full_info, no_orders, no_manager, no_address_match]:
        c.execute(item)
        print(c.fetchall(), '\n\n')


