from flask import Blueprint
from application.controllers import home, auth,dashboard,product
web = Blueprint('web',__name__)

web.add_url_rule('/',view_func=home.index, methods=['GET',"POST"])

#auth Routes
web.add_url_rule('/login',view_func=auth.login, methods=['GET',"POST"])
web.add_url_rule('/register',view_func=auth.register, methods=['GET',"POST"])
web.add_url_rule('/logout',view_func=auth.logout,methods=["GET","POST"])

#dashboard Routes
web.add_url_rule('/dashboard',view_func=dashboard.dashboard, methods=['GET',"POST"])
web.add_url_rule("/dashboard/products", view_func=product.products, methods=["GET","POST"])
