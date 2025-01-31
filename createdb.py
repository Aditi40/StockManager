import sqlite3
import view
# Connect to SQLite database
conn = sqlite3.connect('stock.db')
cursor = conn.cursor()

def execute_query(cursor, query_type):
    try:
        if query_type == 'insert_supplier':
            name = input("Enter the supplier's name: ")
            email = input("Enter the supplier's email: ")
            phone = input("Enter the supplier's phone number: ")
            cursor.execute("INSERT INTO Suppliers (name, contact_email, phone_number) VALUES (?, ?, ?)", (name, email, phone))

        elif query_type == 'get_products':
            supplier_id = int(input("Enter the supplier's ID: "))
            cursor.execute("SELECT * FROM Products WHERE supplier_id = ?", (supplier_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_quantity':
            product_id = int(input("Enter the product's ID: "))
            new_quantity = int(input("Enter the new quantity: "))
            cursor.execute("UPDATE Products SET quantity = ? WHERE product_id = ?", (new_quantity, product_id))

        elif query_type == 'get_order_amount':
            order_id = int(input("Enter the order's ID: "))
            cursor.execute("SELECT total_amount FROM Orders WHERE order_id = ?", (order_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_user':
            user_id = int(input("Enter the user's ID: "))
            cursor.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))

        elif query_type == 'insert_product':
            name = input("Enter the product's name: ")
            description = input("Enter the product's description: ")
            price = float(input("Enter the product's price: "))
            quantity = int(input("Enter the product's quantity: "))
            supplier_id = int(input("Enter the supplier's ID: "))
            cursor.execute("INSERT INTO Products (name, description, price, quantity, supplier_id) VALUES (?, ?, ?, ?, ?)", (name, description, price, quantity, supplier_id))

        elif query_type == 'get_orders':
            customer_id = int(input("Enter the customer's ID: "))
            cursor.execute("SELECT * FROM Orders WHERE customer_id = ?", (customer_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_price':
            product_id = int(input("Enter the product's ID: "))
            new_price = float(input("Enter the new price: "))
            cursor.execute("UPDATE Products SET price = ? WHERE product_id = ?", (new_price, product_id))

        elif query_type == 'get_total_quantity_ordered':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT SUM(quantity_ordered) FROM OrderItems WHERE product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_order':
            order_id = int(input("Enter the order's ID: "))
            cursor.execute("DELETE FROM Orders WHERE order_id = ?", (order_id,))

        elif query_type == 'insert_warehouse':
            name = input("Enter the warehouse's name: ")
            location = input("Enter the warehouse's location: ")
            cursor.execute("INSERT INTO Warehouses (name, location) VALUES (?, ?)", (name, location))

        elif query_type == 'get_stock_movements':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT * FROM StockMovements WHERE product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_warehouse_location':
            warehouse_id = int(input("Enter the warehouse's ID: "))
            new_location = input("Enter the new location: ")
            cursor.execute("UPDATE Warehouses SET location = ? WHERE warehouse_id = ?", (new_location, warehouse_id))

        elif query_type == 'get_total_quantity_change':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT SUM(quantity_change) FROM StockMovements WHERE product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_warehouse':
            warehouse_id = int(input("Enter the warehouse's ID: "))
            cursor.execute("DELETE FROM Warehouses WHERE warehouse_id = ?", (warehouse_id,))

        elif query_type == 'insert_category':
            name = input("Enter the category's name: ")
            cursor.execute("INSERT INTO Categories (name) VALUES (?)", (name,))

        elif query_type == 'update_product_description':
            product_id = int(input("Enter the product's ID: "))
            new_description = input("Enter the new description: ")
            cursor.execute("UPDATE Products SET description = ? WHERE product_id = ?", (new_description, product_id))

        elif query_type == 'get_total_customers':
            cursor.execute("SELECT COUNT(*) FROM Customers")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_category':
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("DELETE FROM Categories WHERE category_id = ?", (category_id,))

        elif query_type == 'insert_customer':
            first_name = input("Enter the customer's first name: ")
            last_name = input("Enter the customer's last name: ")
            email = input("Enter the customer's email: ")
            address = input("Enter the customer's address: ")
            cursor.execute("INSERT INTO Customers (first_name, last_name, email, address) VALUES (?, ?, ?, ?)", (first_name, last_name, email, address))

        elif query_type == 'get_customer_orders':
            customer_id = int(input("Enter the customer's ID: "))
            cursor.execute("SELECT * FROM Orders WHERE customer_id = ?", (customer_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_customer_address':
            customer_id = int(input("Enter the customer's ID: "))
            new_address = input("Enter the new address: ")
            cursor.execute("UPDATE Customers SET address = ? WHERE customer_id = ?", (new_address, customer_id))

        elif query_type == 'get_total_customer_orders':
            customer_id = int(input("Enter the customer's ID: "))
            cursor.execute("SELECT COUNT(*) FROM Orders WHERE customer_id = ?", (customer_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_customer':
            customer_id = int(input("Enter the customer's ID: "))
            cursor.execute("DELETE FROM Customers WHERE customer_id = ?", (customer_id,))

        elif query_type == 'insert_order':
            customer_id = int(input("Enter the customer's ID: "))
            order_date = input("Enter the order date (YYYY-MM-DD): ")
            total_amount = float(input("Enter the total amount: "))
            cursor.execute("INSERT INTO Orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)", (customer_id, order_date, total_amount))

        elif query_type == 'get_order_items':
            order_id = int(input("Enter the order's ID: "))
            cursor.execute("SELECT * FROM OrderItems WHERE order_id = ?", (order_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_order_total':
            order_id = int(input("Enter the order's ID: "))
            new_total = float(input("Enter the new total amount: "))
            cursor.execute("UPDATE Orders SET total_amount = ? WHERE order_id = ?", (new_total, order_id))

        elif query_type == 'get_total_supplier_products':
            supplier_id = int(input("Enter the supplier's ID: "))
            cursor.execute("SELECT COUNT(*) FROM Products WHERE supplier_id = ?", (supplier_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_order':
            order_id = int(input("Enter the order's ID: "))
            cursor.execute("DELETE FROM Orders WHERE order_id = ?", (order_id,))

        elif query_type == 'insert_order_item':
            order_id = int(input("Enter the order's ID: "))
            product_id = int(input("Enter the product's ID: "))
            quantity_ordered = int(input("Enter the quantity ordered: "))
            cursor.execute("INSERT INTO OrderItems (order_id, product_id, quantity_ordered) VALUES (?, ?, ?)", (order_id, product_id, quantity_ordered))

        elif query_type == 'get_orders_on_date':
            order_date = input("Enter the order date (YYYY-MM-DD): ")
            cursor.execute("SELECT * FROM Orders WHERE order_date = ?", (order_date,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_order_item_quantity':
            order_item_id = int(input("Enter the order item's ID: "))
            new_quantity = int(input("Enter the new quantity ordered: "))
            cursor.execute("UPDATE OrderItems SET quantity_ordered = ? WHERE order_item_id = ?", (new_quantity, order_item_id))

        elif query_type == 'get_total_order_items':
            order_id = int(input("Enter the order's ID: "))
            cursor.execute("SELECT COUNT(*) FROM OrderItems WHERE order_id = ?", (order_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_order_item':
            order_item_id = int(input("Enter the order item's ID: "))
            cursor.execute("DELETE FROM OrderItems WHERE order_item_id = ?", (order_item_id,))

        elif query_type == 'insert_stock_movement':
            product_id = int(input("Enter the product's ID: "))
            warehouse_id = int(input("Enter the warehouse's ID: "))
            movement_date = input("Enter the movement date (YYYY-MM-DD): ")
            quantity_change = int(input("Enter the quantity change: "))
            cursor.execute("INSERT INTO StockMovements (product_id, warehouse_id, movement_date, quantity_change) VALUES (?, ?, ?, ?)", (product_id, warehouse_id, movement_date, quantity_change))

        elif query_type == 'get_warehouse_movements':
            warehouse_id = int(input("Enter the warehouse's ID: "))
            cursor.execute("SELECT * FROM StockMovements WHERE warehouse_id = ?", (warehouse_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_stock_movement_quantity':
            movement_id = int(input("Enter the movement's ID: "))
            new_quantity_change = int(input("Enter the new quantity change: "))
            cursor.execute("UPDATE StockMovements SET quantity_change = ? WHERE movement_id = ?", (new_quantity_change, movement_id))

        elif query_type == 'get_total_product_movements':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT COUNT(*) FROM StockMovements WHERE product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_stock_movement':
            movement_id = int(input("Enter the movement's ID: "))
            cursor.execute("DELETE FROM StockMovements WHERE movement_id = ?", (movement_id,))

        elif query_type == 'insert_user':
            username = input("Enter the user's username: ")
            password = input("Enter the user's password: ")
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))

        elif query_type == 'get_user_orders':
            user_id = int(input("Enter the user's ID: "))
            cursor.execute("SELECT * FROM Orders WHERE user_id = ?", (user_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_user_password':
            user_id = int(input("Enter the user's ID: "))
            new_password = input("Enter the new password: ")
            cursor.execute("UPDATE Users SET password = ? WHERE user_id = ?", (new_password, user_id))

        elif query_type == 'get_total_user_orders':
            user_id = int(input("Enter the user's ID: "))
            cursor.execute("SELECT COUNT(*) FROM Orders WHERE user_id = ?", (user_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_user':
            user_id = int(input("Enter the user's ID: "))
            cursor.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))

        elif query_type == 'get_expensive_products':
            price = float(input("Enter the price: "))
            cursor.execute("SELECT * FROM Products WHERE price > ?", (price,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'get_product_suppliers':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT Suppliers.* FROM Suppliers INNER JOIN Products ON Suppliers.supplier_id = Products.supplier_id WHERE Products.product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'get_product_customers':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT Customers.* FROM Customers INNER JOIN Orders ON Customers.customer_id = Orders.customer_id INNER JOIN OrderItems ON Orders.order_id = OrderItems.order_id WHERE OrderItems.product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'get_total_product_quantity':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT SUM(quantity_change) FROM StockMovements WHERE product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'get_product_warehouses':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT Warehouses.* FROM Warehouses INNER JOIN StockMovements ON Warehouses.warehouse_id = StockMovements.warehouse_id WHERE StockMovements.product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'insert_category':
            name = input("Enter the category's name: ")
            cursor.execute("INSERT INTO Categories (name) VALUES (?)", (name,))

        elif query_type == 'get_products_in_category':
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("SELECT * FROM Products WHERE category_id = ?", (category_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_product_description':
            product_id = int(input("Enter the product's ID: "))
            new_description = input("Enter the new description: ")
            cursor.execute("UPDATE Products SET description = ? WHERE product_id = ?", (new_description, product_id))

        elif query_type == 'get_total_customers':
            cursor.execute("SELECT COUNT(*) FROM Customers")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_category':
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("DELETE FROM Categories WHERE category_id = ?", (category_id,))
        elif query_type == 'delete_supplier':
            supplier_id = int(input("Enter the supplier's ID: "))
            cursor.execute("DELETE FROM Suppliers WHERE supplier_id = ?", (supplier_id,))
        elif query_type == 'delete_product':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("DELETE FROM Products WHERE product_id = ?", (product_id,))

        elif query_type == 'insert_customer':
            first_name = input("Enter the customer's first name: ")
            last_name = input("Enter the customer's last name: ")
            email = input("Enter the customer's email: ")
            address = input("Enter the customer's address: ")
            cursor.execute("INSERT INTO Customers (first_name, last_name, email, address) VALUES (?, ?, ?, ?)", (first_name, last_name, email, address))

        elif query_type == 'get_customer_orders':
            customer_id = int(input("Enter the customer's ID: "))
            cursor.execute("SELECT * FROM Orders WHERE customer_id = ?", (customer_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_customer_address':
            customer_id = int(input("Enter the customer's ID: "))
            new_address = input("Enter the new address: ")
            cursor.execute("UPDATE Customers SET address = ? WHERE customer_id = ?", (new_address, customer_id))

        elif query_type == 'get_total_customer_orders':
            customer_id = int(input("Enter the customer's ID: "))
            cursor.execute("SELECT COUNT(*) FROM Orders WHERE customer_id = ?", (customer_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_customer':
            customer_id = int(input("Enter the customer's ID: "))
            cursor.execute("DELETE FROM Customers WHERE customer_id = ?", (customer_id,))

        elif query_type == 'insert_stock_movement':
            product_id = int(input("Enter the product's ID: "))
            warehouse_id = int(input("Enter the warehouse's ID: "))
            movement_date = input("Enter the movement date (YYYY-MM-DD): ")
            quantity_change = int(input("Enter the quantity change: "))
            cursor.execute("INSERT INTO StockMovements (product_id, warehouse_id, movement_date, quantity_change) VALUES (?, ?, ?, ?)", (product_id, warehouse_id, movement_date, quantity_change))

        elif query_type == 'get_warehouse_movements':
            warehouse_id = int(input("Enter the warehouse's ID: "))
            cursor.execute("SELECT * FROM StockMovements WHERE warehouse_id = ?", (warehouse_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_stock_movement_quantity':
            movement_id = int(input("Enter the movement's ID: "))
            new_quantity_change = int(input("Enter the new quantity change: "))
            cursor.execute("UPDATE StockMovements SET quantity_change = ? WHERE movement_id = ?", (new_quantity_change, movement_id))

        elif query_type == 'get_total_product_movements':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT COUNT(*) FROM StockMovements WHERE product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_stock_movement':
            movement_id = int(input("Enter the movement's ID: "))
            cursor.execute("DELETE FROM StockMovements WHERE movement_id = ?", (movement_id,))

        elif query_type == 'insert_product_into_category':
            product_id = int(input("Enter the product's ID: "))
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("INSERT INTO ProductCategories (product_id, category_id) VALUES (?, ?)", (product_id, category_id))

        elif query_type == 'get_product_categories':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT Categories.* FROM Categories INNER JOIN ProductCategories ON Categories.category_id = ProductCategories.category_id WHERE ProductCategories.product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_product_category':
            product_id = int(input("Enter the product's ID: "))
            new_category_id = int(input("Enter the new category's ID: "))
            cursor.execute("UPDATE Categories SET category_id = ? WHERE product_id = ?", (new_category_id, product_id))

        elif query_type == 'get_total_category_products':
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("SELECT COUNT(*) FROM Categories WHERE category_id = ?", (category_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_product_category':
            product_id = int(input("Enter the product's ID: "))
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("DELETE FROM ProductCategories WHERE product_id = ? AND category_id = ?", (product_id, category_id))

        elif query_type == 'insert_customer_order':
            customer_id = int(input("Enter the customer's ID: "))
            order_date = input("Enter the order date (YYYY-MM-DD): ")
            total_amount = float(input("Enter the total amount: "))
            cursor.execute("INSERT INTO Orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)", (customer_id, order_date, total_amount))

        elif query_type == 'get_product_customers':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT Customers.* FROM Customers INNER JOIN Orders ON Customers.customer_id = Orders.customer_id INNER JOIN OrderItems ON Orders.order_id = OrderItems.order_id WHERE OrderItems.product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_order_date':
            order_id = int(input("Enter the order's ID: "))
            new_order_date = input("Enter the new order date (YYYY-MM-DD): ")
            cursor.execute("UPDATE Orders SET order_date = ? WHERE order_id = ?", (new_order_date, order_id))

        elif query_type == 'get_total_orders_on_date':
            order_date = input("Enter the order date (YYYY-MM-DD): ")
            cursor.execute("SELECT COUNT(*) FROM Orders WHERE order_date = ?", (order_date,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_customer_order':
            customer_id = int(input("Enter the customer's ID: "))
            order_id = int(input("Enter the order's ID: "))
            cursor.execute("DELETE FROM Orders WHERE customer_id = ? AND order_id = ?", (customer_id, order_id))

        elif query_type == 'insert_product_movement':
            product_id = int(input("Enter the product's ID: "))
            warehouse_id = int(input("Enter the warehouse's ID: "))
            movement_date = input("Enter the movement date (YYYY-MM-DD): ")
            quantity_change = int(input("Enter the quantity change: "))
            cursor.execute("INSERT INTO StockMovements (product_id, warehouse_id, movement_date, quantity_change) VALUES (?, ?, ?, ?)", (product_id, warehouse_id, movement_date, quantity_change))

        elif query_type == 'get_warehouse_products':
            warehouse_id = int(input("Enter the warehouse's ID: "))
            cursor.execute("SELECT Products.* FROM Products INNER JOIN StockMovements ON Products.product_id = StockMovements.product_id WHERE StockMovements.warehouse_id = ?", (warehouse_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_movement_date':
            movement_id = int(input("Enter the movement's ID: "))
            new_movement_date = input("Enter the new movement date (YYYY-MM-DD): ")
            cursor.execute("UPDATE StockMovements SET movement_date = ? WHERE movement_id = ?", (new_movement_date, movement_id))

        elif query_type == 'get_total_product_movements_in_warehouse':
            product_id = int(input("Enter the product's ID: "))
            warehouse_id = int(input("Enter the warehouse's ID: "))
            cursor.execute("SELECT COUNT(*) FROM StockMovements WHERE product_id = ? AND warehouse_id = ?", (product_id, warehouse_id))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_product_movement':
            product_id = int(input("Enter the product's ID: "))
            warehouse_id = int(input("Enter the warehouse's ID: "))
            movement_id = int(input("Enter the movement's ID: "))
            cursor.execute("DELETE FROM StockMovements WHERE product_id = ? AND warehouse_id = ? AND movement_id = ?", (product_id, warehouse_id, movement_id))

        elif query_type == 'insert_product_into_category':
            product_id = int(input("Enter the product's ID: "))
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("INSERT INTO ProductCategories (product_id, category_id) VALUES (?, ?)", (product_id, category_id))

        elif query_type == 'get_product_categories':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT Categories.* FROM Categories INNER JOIN Categories ON Categories.category_id = ProductCategories.category_id WHERE ProductCategories.product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_product_category':
            product_id = int(input("Enter the product's ID: "))
            new_category_id = int(input("Enter the new category's ID: "))
            cursor.execute("UPDATE ProductCategories SET category_id = ? WHERE product_id = ?", (new_category_id, product_id))

        elif query_type == 'get_total_category_products':
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("SELECT COUNT(*) FROM Categories WHERE category_id = ?", (category_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'delete_product_category':
            product_id = int(input("Enter the product's ID: "))
            category_id = int(input("Enter the category's ID: "))
            cursor.execute("DELETE FROM Categories WHERE product_id = ? AND category_id = ?", (product_id, category_id))

        elif query_type == 'insert_customer_order':
            customer_id = int(input("Enter the customer's ID: "))
            order_date = input("Enter the order date (YYYY-MM-DD): ")
            total_amount = float(input("Enter the total amount: "))
            cursor.execute("INSERT INTO Orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)", (customer_id, order_date, total_amount))

        elif query_type == 'get_product_customers':
            product_id = int(input("Enter the product's ID: "))
            cursor.execute("SELECT Customers.* FROM Customers INNER JOIN Orders ON Customers.customer_id = Orders.customer_id INNER JOIN OrderItems ON Orders.order_id = OrderItems.order_id WHERE OrderItems.product_id = ?", (product_id,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("\n")
        elif query_type == 'update_order_date':
            order_id = int(input("Enter the order's ID: "))
            new_order_date = input("Enter the new order date (YYYY-MM-DD): ")
            cursor.execute("UPDATE Orders SET order_date = ? WHERE order_id = ?", (new_order_date, order_id))

        else:
            print("Invalid query type. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    conn.commit()


while True:
    temp = input("What do you want to do? : ")
    if temp == "leave":
        conn.close()
        quit()
    else:
        execute_query(cursor,temp)
        view.view_all_data()

conn.close()

#Kindly have sqlite3 viewing application for better understanding

