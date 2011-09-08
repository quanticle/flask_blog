import sqlite3

class User:
    def __init__(self, username, password_hash, real_name):
        self.username = username
        self.password_hash = password_hash
        self.real_name = real_name

    def get_username(self):
        return self.username

    def get_password_hash(self):
        return self.password_hash

    def get_real_name(self):
        return self.real_name

    def set_username(self, username):
        self.username = username

    def set_password_hash(self, new_password_hash):
        self.password_hash = new_password_hash

    def set_real_name(self, new_real_name):
        self.real_name = new_real_name

