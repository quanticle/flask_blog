import sqlite3

class User:
    def __init__(self, username, password_hash, realname, salt):
        self.username = username
        self.password_hash = password_hash
        self.salt = salt
        self.realname = realname
    

    def get_username(self):
        return self.username

    def get_password_hash(self):
        return self.password_hash

    def get_salt(self):
        return self.salt

    def get_real_name(self):
        return self.real_name

