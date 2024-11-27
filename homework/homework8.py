import sqlite3

def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_data(db_name, sql, data):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.executemany(sql, data)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

create_table_countries = """
CREATE TABLE IF NOT EXISTS countries(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT NOT NULL
)
"""

create_table_cities = """
CREATE TABLE IF NOT EXISTS cities(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT NOT NULL,
     area FLOAT DEFAULT 0,
     country_id INTEGER,
     FOREIGN KEY (country_id) REFERENCES countries (id)
)
"""

create_table_students = """
CREATE TABLE IF NOT EXISTS students(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     first_name TEXT NOT NULL,
     last_name TEXT NOT NULL,
     city_id INTEGER,
     FOREIGN KEY (city_id) REFERENCES cities (id)
)
"""

def get_cities(db_name):
    sql = "SELECT id, title FROM cities"
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
        return []

def get_students_by_city(db_name, city_id):
    sql = """
    SELECT 
        students.first_name, 
        students.last_name, 
        countries.title AS country,
        cities.title AS city, 
        cities.area
    FROM students
    LEFT JOIN cities ON students.city_id = cities.id
    LEFT JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    """
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (city_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
        return []

def display_menu(db_name):
    while True:
        print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
        cities = get_cities(db_name)
        if not cities:
            print("Нет данных о городах.")
            break
        for city in cities:
            print(f"{city[0]}. {city[1]}")
        try:
            city_id = int(input("Введите id города: "))
        except ValueError:
            print("Введите корректное число.")
            continue
        if city_id == 0:
            print("Выход из программы.")
            break
        students = get_students_by_city(db_name, city_id)
        if students:
            print("\nСписок студентов:")
            for student in students:
                print(
                    f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2] or 'Не указана'}, Город: {student[3]}, Площадь города: {student[4]} км²")
        else:
            print("В этом городе пока нет студентов.")

db_name = 'hw8.db'
create_table(db_name, create_table_countries)
create_table(db_name, create_table_cities)
create_table(db_name, create_table_students)

insert_data(db_name, "INSERT INTO countries (title) VALUES (?)", [
    ('Германия',),
    ('Турция',),
    ('Россия',)
])

insert_data(db_name, "INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", [
    ('Москва', 2511, 3),
    ('Стамбул', 5343, 2),
    ('Берлин', 891.8, 1),
    ('Санкт-Петербург', 1439, 3),
    ('Мюнхен', 310.7, 1),
    ('Анкара', 2451, 2),
    ('Казань', 425.3, 3)
])

insert_data(db_name, "INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", [
    ('Жибек', 'Акылбек кызы', 1),
    ('Шамиль', 'Эскендеров', 1),
    ('Алим', 'Эскендеров', 2),
    ('Дария', 'Таирова', 3),
    ('Жибек', 'Романбекова', 3),
    ('Гуляим', 'Ильясова', 3),
    ('Атай', 'Салымбеков', 4),
    ('Наргиз', 'Сабырова', 4),
    ('Эскен', 'Сулеев', 5),
    ('Камал', 'Абдулаев', 6),
    ('Айлин', 'Калдыбаева', 6),
    ('Даша', 'Зинина', 6),
    ('Арина', 'Варнак', 7),
    ('Медина', 'Манасова', 7),
    ('Акжол', 'Ахматов', 7)
])

display_menu(db_name)
