import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            connection.commit()
            print("Таблица создана")
    except sqlite3.Error as e:
        print(e)

def insert_product(db_name, product):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES(?,?,?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
    except sqlite3.Error as error:
        print(f"Ошибка при добавлении товара: {error}")

def insert_15_different_products(db_name):
    products = [
        ('Milk', 25.50, 50),
        ('Sugar', 30.00, 25),
        ('Salt', 10.00, 40),
        ('Rice', 40.00, 35),
        ('Bread', 14.00, 30),
        ('Butter', 34.25, 20),
        ('Cheese', 80.00, 15),
        ('Eggs', 80.50, 50),
        ('Pasta', 35.00, 20),
        ('Tea', 55.00, 10),
        ('Coffee', 120.00, 5),
        ('Chocolate', 75.00, 8),
        ('Juice', 50.00, 12),
        ('Water', 20.00, 60),
        ('Yogurt', 25.00, 15)
    ]
    for product in products:
        insert_product(db_name, product)

def update_quantity(db_name, product_id, new_quantity):
    sql = '''UPDATE products
             SET quantity = ?
             WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (new_quantity, product_id))
            connection.commit()
            print(f"Количество товара с ID {product_id} обновлено до {new_quantity}.")
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении количества: {e}")

def update_price(db_name, product_id, new_price):
    sql = '''UPDATE products
             SET price = ?
             WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (new_price, product_id))
            connection.commit()
            print(f"Цена товара с ID {product_id} обновлена до {new_price}.")
    except sqlite3.Error as e:
        print(f"Ошибка при обновлении цены: {e}")

def delete_product(db_name, product_id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (product_id,))
            connection.commit()
            print(f"Товар с ID {product_id} удалён.")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении товара: {e}")

def select_all_products(db_name):
    sql = "SELECT * FROM products"
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            if rows:
                print("Все товары:")
                for row in rows:
                    print(row)
            else:
                print("Таблица пуста.")
    except sqlite3.Error as e:
        print(f"Ошибка при выборе товаров: {e}")

def select_cheap_products(db_name, price_limit, quantity_limit):
    sql = '''SELECT * FROM products
             WHERE price < ? AND quantity > ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit, quantity_limit))
            rows = cursor.fetchall()
            if rows:
                print(f"Товары дешевле {price_limit} сом и с количеством больше {quantity_limit}:")
                for row in rows:
                    print(row)
            else:
                print("Нет товаров, подходящих под критерии.")
    except sqlite3.Error as e:
        print(f"Ошибка при выборке дешевых товаров: {e}")

def search_products_by_name(db_name, search_query):
    sql = '''SELECT * FROM products
             WHERE product_title LIKE ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, ('%' + search_query + '%',))
            rows = cursor.fetchall()
            if rows:
                print(f"Результаты поиска по запросу '{search_query}':")
                for row in rows:
                    print(row)
            else:
                print(f"Нет товаров, соответствующих запросу '{search_query}'.")
    except sqlite3.Error as e:
        print(f"Ошибка при поиске товаров: {e}")

sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

database_name = 'hw.db'
my_connection = create_connection(database_name)

if my_connection is not None:
    print('Соединение с базой данных установлено')
    create_table(database_name, sql_to_create_products_table)
    insert_15_different_products(database_name)
    select_all_products(database_name)
    update_quantity(database_name, 1, 85)
    update_price(database_name, 2, 20.00)
    delete_product(database_name, 3)
    select_cheap_products(database_name, 30, 3)
    search_products_by_name(database_name, 'Milk')
