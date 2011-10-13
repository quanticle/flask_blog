import sqlite3
from datetime import datetime
from controllers.user_controller import UserController
from controllers.post_controller import PostController
from models.post import Post

def main():
    db_connection = sqlite3.connect("blog_db.sqlite3")
    sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras vehicula malesuada turpis, id tempus ligula eleifend vel. Vivamus ante ligula, tincidunt at egestas bibendum, fringilla non lorem. Fusce venenatis urna quis nibh ullamcorper sed consequat arcu blandit. In hac habitasse platea dictumst. Nullam nibh leo, eleifend eget cursus eget, sagittis vel mi. Sed consectetur massa et nulla iaculis pretium. Nullam fringilla euismod quam, ac aliquet erat pharetra non. Fusce commodo sagittis nisi interdum molestie. Fusce odio tortor, dapibus non dictum vitae, bibendum nec nulla."""
    post_title = "Test Post"
    post_controller = PostController(db_connection)
    user_controller = UserController(db_connection)
    post_author = user_controller.get_user("Test2")
    test_post = Post(post_title, str(datetime.now()), post_author, post_text=sample_text)
    saved_post = post_controller.add_post(test_post)
    print "Saved Post ID: %d" % saved_post.get_id()

if __name__ == "__main__":
    main()
    
