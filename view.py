import sqlite3

def view_all_data():
    # Connect to SQLite database
    conn = sqlite3.connect('stock.db')
    cursor = conn.cursor()

    # List of all tables in the database
    tables = ['Suppliers', 'Products', 'Categories', 'Customers', 'Orders', 'OrderItems', 'Warehouses', 'StockMovements', 'Users']

    for table in tables:
        print(f"Table: {table}")
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")

    # Close the connection
    conn.close()

