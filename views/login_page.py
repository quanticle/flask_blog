from jinja2 import Environment, PackageLoader
from controllers.user_controller import UserController
from config.blog_config import config

def show_login_page(destination):
    template_environment = Environment(loader=PackageLoader("views", "templates"))
    template = template_environment.get_template("login_page.html")
    return template.render(blog_title = config['blog_title'])
