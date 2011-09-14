import sqlite3

create_user_sql = """CREATE TABLE users (username TEXT, password_hash TEXT, salt TEXT, PRIMARY KEY (username))"""
create_post_sql = """CREATE TABLE posts (post_title TEXT, post_date TEXT, post_file TEXT, post_author TEXT,
FOREIGN KEY(post_author) REFERENCES users(username))"""

def create_database():
    db_conn = sqlite3.connect("blog_db.sqlite3")
    db_curs = db_conn.cursor()
    db_curs.execute(create_user_sql)
    db_curs.execute(create_post_sql)


if __name__ == "__main__":
    create_database()
    print "Database created successfully."
    
