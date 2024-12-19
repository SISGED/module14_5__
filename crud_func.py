import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')

    connection.commit()


def populate_products():
    cursor.executescript('''
        INSERT INTO Products (title, description, price) VALUES (
            "Икра красная", "S", 100);
        INSERT INTO Products (title, description, price) VALUES (
            "Икра красная", "L", 200);
        INSERT INTO Products (title, description, price) VALUES (
            "Икра красная", "XL", 300);
        INSERT INTO Products (title, description, price) VALUES (
            "Икра черная", "XXXL", 1000);
    ''')
    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


def add_user(username, email, age, balance=1000):
    cursor.execute(
        'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
        (username, email, age, balance))
    connection.commit()


def is_included(username):
    return True \
        if cursor.execute('SELECT COUNT(*) from Users WHERE username = ?',
                          (username, )).fetchone()[0] \
        else False


def products_is_empty():
    return not cursor.execute('SELECT COUNT(*) from Products').fetchone()[0]


if __name__ == '__main__':
    initiate_db()
    if products_is_empty():
        populate_products()
    connection.close()