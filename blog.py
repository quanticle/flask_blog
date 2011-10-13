from flask import Flask
from views import all_posts, add_post_form
from config.blog_config import config
import sqlite3

app = Flask(__name__)
app.debug = True
@app.route('/')
def root():
    db_path = config['db_location']
    db_connection = sqlite3.connect(db_path)
    return all_posts.show_all_posts(db_connection)

@app.route('/add_post/')
def add_post():
    if request.method == "POST":
        post_title = request.form['post_title']
        post_text = request.form['post_text']
        add_post_form.add_post(title, text)
    else: 
        return add_post_form.show_add_post()

if __name__ == '__main__':
    app.run()
