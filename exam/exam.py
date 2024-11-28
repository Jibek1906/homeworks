import sqlite3

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

create_table_categories = """
    CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150)
    )
"""

create_table_products = """
    CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250),
    category_code VARCHAR(2),
    unit_price FLOAT,
    stock_quantity INTEGER,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories (code),
    FOREIGN KEY (store_id) REFERENCES stores (store_id)
    )
"""

create_table_stores = """
    CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY,
    title VARCHAR(100)
    )
"""

def get_store(db_name):
    sql = "SELECT store_id, title FROM stores"
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
        return []

def get_products_by_store(db_name, store_id):
    sql = """
        SELECT 
            p.title AS product_title,
            c.title AS category_title,
            p.unit_price,
            p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    """
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (store_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
        return []

def display_menu(db_name):
    while True:
        print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
        shops = get_store(db_name)
        if not shops:
            print("Нет данных о магазинах")
            break
        for shop in shops:
            print(f"{shop[0]}. {shop[1]}")
        try:
            store_id = int(input("Введите id магазина: "))
        except ValueError:
            print("Введите корректное число.")
            continue
        if store_id == 0:
            print("Выход из программы")
            break
        products = get_products_by_store(db_name, store_id)
        if products:
            print("\nСписок продуктов:")
            for product in products:
                print(
                    f"Название продукта: {product[0]}\n"
                    f"Категория: {product[1]}\n"
                    f"Цена: {product[2]}\n"
                    f"Количество на складе: {product[3]}")
        else:
            print("В этом магазине ничего нет")

db_name = 'exam.db'
# create_table(db_name, create_table_categories)
# create_table(db_name, create_table_products)
# create_table(db_name, create_table_stores)

display_menu(db_name)
