from jinja2 import Environment, PackageLoader
from models.post import Post
from models.user import User
from controllers.post_controller import PostController
from controllers.user_controller import UserController
from config.blog_config import config

def add_post(post_title, post_text):
    pass
def show_add_post():
    template_environment = Environment(loader=PackageLoader('views', 'templates'))
    template = template_environment.get_template('add_post.html')
    return template.render(blog_title=config['blog_title'])
    
