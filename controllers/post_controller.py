import sqlite3
import os

class PostController:
    def __init__(self, db_location, post_folder):
        self.db_location = db_location
        self.post_folder = post_folder

    