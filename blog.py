from flask import Flask, request
from views import all_posts, add_post_form, login_page
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

@app.route('/login/<destination>')
def login():
    if request.method == "POST":
        #Handle login handling here
        pass
    else: 
        return login_page.show_login_page(destination)
if __name__ == '__main__':
    app.run()
