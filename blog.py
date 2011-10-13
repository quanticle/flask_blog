from flask import Flask
from views import all_posts
from config.blog_config import config
import sqlite3

app = Flask(__name__)
app.debug = True
@app.route('/')
def root():
    db_path = config['db_location']
    db_connection = sqlite3.connect(db_path)
    return all_posts.show_all_posts(db_connection)


if __name__ == '__main__':
    app.run()
