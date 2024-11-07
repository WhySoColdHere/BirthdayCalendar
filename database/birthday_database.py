from sqlite3 import connect


class BirthdayDatabase:
    def __init__(self):
        self.connection = connect("birthday_db")
        self.cursor = self.connection.cursor()
        self._create_db()

    def _create_db(self):
        self.cursor.execute("""
        CREATE TABLE birthdays(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date DATE
        )""")

    def read(self, person=None):
        pass  # if person: (берем только одного человека) else: (возвращаем всех)

    def update(self, first_name, last_name, date):
        pass

    def remove(self, first_name, last_name):
        pass

    def __del__(self):
        self.connection.close()
