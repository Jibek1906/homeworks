import sqlite3
from audioop import error


# SQL (Structured Query Language) — это язык, который используется для работы с базами данных. Он позволяет создавать, изменять, удалять и получать данные из базы. Простыми словами, это как язык общения с базой данных, чтобы узнать, что в ней хранится, или изменить данные.
# субд - система управления базами данных
# система - набор библиотек и инструментов, которые позволяют работать с базами данных
# CRUD - CREATE READ UPDATE DELETE основные операции для базы данных
# таблицы - колонки это аттрибуты, а строки записи
# при взаимодействии с третьей стороной всегда код помешаем в try
# запросы помещаются в '''''' в самом sql также
# Varchar - для небольшого объема текста, text - для более крупного объема информации
# NULL - по умолчанию пустая это значит не обязательна для заполнения
# чтобы прогнать любой sql запрос, нам нужно получить объект cursor
# в sql тип данных str и date всегда в одинарных кавычках ''
# dml - data manipulation language это операции, которые вносят изменения в нашу базу данных UPDATE DELETE ADD
# select
# full_name, is_married, (case # это if в sql
# when is_married = 0 then 'single'
# when is_married= 1 then 'married'
# else 'unknown' end) as marital_status
# from employees
# сортировка в sql select * from employees order by salary
# сортировка в sql select * from employees order by salary desc - обратная сортировка


# def create_connection(db_name):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as e:
#         print(e)
#     return connection
#
#
# def create_table(connection, create_table_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#     except sqlite3.Error as e:
#         print(e)
#
#
# def insert_employee(connection, employee):
#     sql = '''INSERT INTO employees
#     (full_name, salary, hobby, birth_date, is_married)
#     VALUES (?, ?, ?, ?, ?) '''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, employee)
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)



def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            # execute - это метод объекта cursor, который принимает SQL-запрос в виде строки и выполняет его. В данном случае он используется для выполнения команды создания таблицы
    except sqlite3.Error as e:
        print(e)


def insert_employee(db_name, employee):
    sql = '''INSERT INTO employees
    (full_name, salary, hobby, birth_date, is_married)
    VALUES (?, ?, ?, ?, ?) '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
            connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_employee(db_name, employee):
    sql = '''UPDATE employees SET salary = ?, is_married = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
    except sqlite3.Error as e:
        print(e)


def delete_employee(db_name, id):
    sql = '''DELETE FROM employees WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)


def select_all_employees(db_name):
    sql = '''SELECT * FROM employees'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_employees_by_salary(db_name, salary_limit):
    sql = '''SELECT * FROM employees WHERE salary >= ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (salary_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

sql_to_create_employees_table = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(200) NOT NULL,
    salary FLOAT(10,2) NOT NULL DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
)
'''

database_name = 'group_48.db'
create_table(database_name, sql_to_create_employees_table)

# my_connection = create_connection(database_name)
# if my_connection is not None:
#     print('Successfully connected to database')
#     # create_table(my_connection, sql_to_create_employees_table)
#     insert_employee(my_connection,
#                     ('Jibek Manasova', 2400.5, 'Programming', '2000-01-25', False))
#     my_connection.close()

# insert_employee(database_name, ('Jibek Manasova', 2400.5, 'Programming', '2000-01-25', False))
# insert_employee(database_name, ('Mark Daniels', 1500.0, 'Football', '1999-01-02', False))
# insert_employee(database_name, ('Alex Brilliant', 2300.5, None, '1989-12-31', True))
# insert_employee(database_name, ('Diana Julls', 1800.0, 'Programming', '2005-01-22', True))
# insert_employee(database_name, ('Michael Corse', 1800.0, 'Football', '2001-09-17', True))
# insert_employee(database_name, ('Jack Moris', 2100.2, 'Programming', '2001-07-12', True))
# insert_employee(database_name, ('Viola Manilson', 1750.82, None, '1991-03-01', False))
# insert_employee(database_name, ('Joanna Moris', 1000.0, 'Football', '2004-04-13', False))
# insert_employee(database_name, ('Peter Parker', 2000.0, 'Programming', '2002-11-28', False))
# insert_employee(database_name, ('Paula Parkerson', 800.09, None, '2001-11-28', True))
# insert_employee(database_name, ('George Newel', 1320.0, 'Programming', '1981-01-24', True))
# insert_employee(database_name, ('Miranda Alistoun', 2500.55, 'Football', '1997-12-22', False))
# insert_employee(database_name, ('Valeria Hillton', 2000, 'Football', '1977-10-28', True))
# insert_employee(database_name, ('Jannet Miler', 2100.9, 'Programming', '1997-02-02', True))
# insert_employee(database_name, ('William Tokenson', 1500, None, '1999-12-12', False))
# insert_employee(database_name, ('Shanty Morani', 1200.6, None, '1989-08-13', False))
# insert_employee(database_name, ('Fiona Giordano', 900.12, 'Football', '1977-01-15', True))

# update_employee(database_name, (2500, True, 2))
# delete_employee(database_name, 2)
# select_all_employees(database_name)
select_employees_by_salary(database_name, 2300)