from sqlite3 import connect


class BirthdayDatabase:
    def __init__(self):
        self.connection = connect("database/birthday.db")
        self.cursor = self.connection.cursor()
        self._create_db()

    def _create_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Birthdays (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            birthday_date DATE NOT NULL
        )""")

        self.connection.commit()

    def add(self, cur_first_name, cur_last_name, cur_date):
        self.cursor.execute(
            'INSERT INTO Birthdays (first_name, last_name, birthday_date) VALUES (?, ?, ?)',
            (cur_first_name, cur_last_name, cur_date)
        )

        self.connection.commit()

    def read(self, person=None):
        # if person: (берем только одного человека) else: (возвращаем всех)
        self.connection.commit()

    def update(self, first_name, last_name, date):
        self.connection.commit()

    def remove(self, first_name, last_name):
        self.connection.commit()

    def __del__(self):
        self.connection.commit()
        self.connection.close()
