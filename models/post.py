import sqlite3
import user

class Post:
    def __init__(self, post_title, post_date, post_author_id, post_id=None,  post_text=None):
        self.title = post
        self.date = post_date
        self.author_id = post_author_id

        if post_id != None:
            self.post_id = post_id

        if post_text != None:
            self.text = post_text

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def get_date(self):
        return self.date

    def get_id(self):
        return self.post_id
        
    def get_author(self):
        return self.author_id

    def set_title(self, post_title):
        self.title = post_title

    def set_date(self, post_date):
        self.date = post_date

    def set_text(self, post_text):
        self.text = post_text
        
    def set_author(self, post_author_id):
        self.author_id = post_author_id
