#! /usr/bin/python

import sqlite3

class UserController:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def get_user(self, username):
        select_user_sql = "SELECT username, password_hash, salt FROM users WHERE username = ?"
        cursor = self.db_connection.cursor()
        cursor.execute(select_user_sql, username)
        row_list = cursor.fetchall()
        if len(row_list) < 1:
            return None
        else:
            db_row = row_list[0]
            retrieved_user = User(db_row['username'], db_row['password_hash'], db_row['salt'])
            return retrieved_user

