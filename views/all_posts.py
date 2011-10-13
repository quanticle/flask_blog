from jinja2 import Environment, PackageLoader
from models.post import Post
from controllers.post_controller import PostController
from config.blog_config import config

def show_all_posts(db_connection):
    post_controller = PostController(db_connection)
    post_list = post_controller.get_all_posts()
    template_environment = Environment(loader=PackageLoader('views', 'templates'))
    template = template_environment.get_template('all_posts.html')
    return template.render(blog_title=config['blog_title'], post_list = post_list)
