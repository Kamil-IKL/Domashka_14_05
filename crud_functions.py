import random
import sqlite3

connection = sqlite3.connect('bot_product.db')
cursor = connection.cursor()


def initiate_product_db():
    connection = sqlite3.connect('bot_product.db')
    cursor = connection.cursor()

    # для создания БД Products
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    image TEXT NOT NULL
    );
    """)


# Создаю БД Products
initiate_product_db()

# стираю все строки в БДешке (для обновления, чтобы не накапливались данные)
cursor.execute("DELETE FROM Products")

# добавляю с использованием цикла for
"""
изменил интерацию с учетом картинок(c 5 по 9 картинки)
"""
for i in range(5, 10):
    cursor.execute("INSERT INTO Products (title, description, price, image) VALUES (?, ?, ?, ?)",
                   (f"Product{i}", f"info{i}", int(i * 100), f'Image/{i}.png'))


def get_all_products():
    connection = sqlite3.connect('bot_product.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()  # сохраняем изменения
    connection.close()
    return products


# запускаю функцию и дальше использую переменную в телеграм-боте
Products = get_all_products()

# ДЛЯ ПРОВЕРКИ
# print(get_all_products())
# for user in get_all_products():
#     title, info, price, image = user[1], user[2], user[3], user[4]
#     print(f"Продукт: {title} | Описание: {info} | Цена: {price} | Картинка: {image}")

connection.commit()
connection.close()


def initiate_db():
    connection = sqlite3.connect('bot_users.db')
    cursor = connection.cursor()

    # для создания БД Users определяю поля
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT  NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    """)


# создаю БД Users
initiate_db()


def add_user(username, email, age):
    """ функция для добавления нового пользователя в БД с балансом = 1000 """
    connection = sqlite3.connect('bot_users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    """функция для проверки, есть ли данный пользователь в БД ?"""
    connection = sqlite3.connect('bot_users.db')
    cursor = connection.cursor()
    chek_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    connection.commit()
    connection.close()
    return chek_user

# """ СДЕЛАЛ ДЛЯ ПРОВЕРКИ """
# # стираю все строки в БД (для обновления, чтобы не накапливались данные)
# cursor.execute("DELETE FROM Users")
#
# # добавляю пользователей с произвольным возрастом от 18 до 60
# for i in range(1, 5):
#     add_user(f'User{i}', f'example{i}@mail.ru', f'{random.randint(18, 60)}')
#
# # вывод на консоль
# print(is_included('User2'))
# print(is_included('User6'))


# connection.commit()
# connection.close()
