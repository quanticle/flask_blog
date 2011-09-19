#! /usr/bin/python

import sqlite3
from models.user import User
class UserController:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def add_user(self, user):
        """Adds a user to the database"""
        sql = r'INSERT INTO users (username, realname, password_hash, salt) VALUES (?, ?, ?, ?)'
        db_cursor = self.db_connection.cursor() 
        db_cursor.execute(sql, (user.get_username(), user.get_real_name(), user.get_password_hash(), user.get_salt()))
        db_cursor.close()

    def get_user(self, username):
        """Retrieves a user from the database, given a username"""
        select_user_sql = "SELECT username, password_hash, realname, salt FROM users WHERE username = ?"
        cursor = self.db_connection.cursor()
        cursor.execute(select_user_sql, username)
        row_list = cursor.fetchall()
        if len(row_list) < 1:
            cursor.close()
            return None
        else:
            db_row = row_list[0]
            retrieved_user = User(db_row['username'], db_row['password_hash'], db_row['realname'], db_row['salt'])
            cursor.close()
            return retrieved_user

