from datetime import datetime, timedelta
from collections import defaultdict

import psycopg2
from data import config

# con = psycopg2.connect(
#     database=config.DATABASE,
#     user=config.USER,
#     password=config.PASSWORD,
#     host=config.HOST
# )


# sql = con.cursor()
# sql.execute(f"DELETE FROM users")
# con.commit()


class Database:
    def __init__(self, basename):
        self.db = basename
        self.sql = self.db.cursor()

    def add_user(self, user_id, username, num_of_subs, percent, video_id):
        with self.db:
            today = datetime.now().date()
            data = today + timedelta(days=7)
            self.sql.execute(
                f"INSERT INTO users VALUES({user_id}, '@{username}', '{num_of_subs}', '{percent}', '{video_id}', {1}, '{data}')")

    def check_verification(self, user_id):
        with self.db:
            self.sql.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
            if len(self.sql.fetchall()) == 0:
                return 0
            return 1

    def update_account(self, user_id, num_of_subs, percent):
        with self.db:
            self.sql.execute(
                f"UPDATE users SET num_of_subs='{num_of_subs}', percent='{percent}' WHERE user_id = {user_id}")

    def delete_account(self, user_id):
        with self.db:
            self.sql.execute(f"DELETE FROM users WHERE user_id = {user_id}")

    def select_users(self):
        with self.db:
            self.sql.execute(f"SELECT * FROM users")
            users = self.sql.fetchall()
            return users

    def change_access(self, username, access):
        with self.db:
            self.sql.execute(f"SELECT * FROM users WHERE username= '{username}'")
            if len(self.sql.fetchall()) == 0:
                return "Вы ввели неправильный username"
            today = datetime.now().date()
            if access == 1:
                data = today + timedelta(days=30)
            else:
                data = today
            self.sql.execute(
                f"UPDATE users SET access={access}, date='{data}' WHERE username = '{username}'")
            return "Доступ пользователя обновлен"

    def select_one_user(self, username):
        with self.db:
            self.sql.execute(f"SELECT user_id FROM users WHERE username= '{username}'")
            return self.sql.fetchone()[0]

    def show_data_user(self, user_id):
        with self.db:
            self.sql.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
            return self.sql.fetchone()


# db = Database(con)
# print(db.show_data_user(956405195))
