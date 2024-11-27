import sqlite3
def update_employee(db_name, employee):
    sql = """ UPDATE employees SET salary = ? WHERE id = ?
    """
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_employee(db_name, employee):
    sql = """ INSERT INTO employees(name, salary, age)
    VALUES(?,?,?)
    """
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_employee(db_name, id):
    sql = """ DELETE FROM employees WHERE id = ?
    """
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def select_all_employess(db_name):
    sql = """ SELECT * FROM employees
    """
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows =  cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)
