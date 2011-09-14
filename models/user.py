import sqlite3

class User:
    def __init__(self, username, password_hash, salt):
        self.username = username
        self.password_hash = password_hash
        self.salt = salt
    
    def get_username(self):
        return self.username

    def get_password_hash(self):
        return self.password_hash

    def get_salt(self):
        return self.salt
