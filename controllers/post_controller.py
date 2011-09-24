import sqlite3
import os
from models.user import User
from models.post import Post
from controllers.user_controller import UserController

class PostNotFoundException: pass
class PostController:
    def __init__(self, db_connection, post_folder):
        self.db_connection = db_connection
        self.post_folder = post_folder
    
    def get_post(self, post_id):
        db_cursor = self.db_connection.cursor()
        sql = "SELECT rowid, post_title, post_date, post_file, post_author FROM posts WHERE post_id = ?"
        db_cursor.execute(sql, (post_id))
        db_results = db_cursor.fetchall()
        if len(db_results) < 1:
            raise PostNotFoundException()
        else:
            db_row = db_results[0]
            post_id = db_row[0]
            title = db_row[1]
            date = db_row[2]
            filename = db_row[3]
            post_text = _get_post_text(filename)
            author = _get_post_author(db_row[4])
            post = Post(title, date, author, post_id, post_text)
            return post
            

    def _get_post_text(self, post_file):
        post_text = open(post_file).read()
        return post_text
    
    def _get_post_author(self, authorid):
        controller = UserController(self.db_connection)
        user = UserController.get_user(post_author)
        return user
