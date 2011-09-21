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
        self.db_connection.commit()

    def get_user(self, username):
        """Retrieves a user from the database, given a username"""
        select_user_sql = r"SELECT username, password_hash, realname, salt FROM users WHERE username = ?"
        cursor = self.db_connection.cursor()
        cursor.execute(select_user_sql, [username])
        row_list = cursor.fetchall()
        if len(row_list) < 1:
            cursor.close()
            return None
        else:
            db_row = row_list[0]
            #SQLite 3, Y U NO USE DICTIONARY TO RETURN DATA?
            retrieved_user = User(db_row[0], db_row[1], db_row[2], db_row[3])
            cursor.close()
            return retrieved_user

