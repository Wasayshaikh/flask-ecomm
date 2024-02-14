from application.controllers.Controller import Controller
from application.models import databaseSession, Products, ProductMetaData
class ProductController(Controller):
    def __init__(self):
        pass
    def products(self):
        products = databaseSession.query(Products).all()
        data = {"title":"Products", "products":products}
        return self.render("dashboard/product/product", data)
    def add_product(self):
        pass
    def edit_product(self):
        pass
    def delete_product(self):
        pass