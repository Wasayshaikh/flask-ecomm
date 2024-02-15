from application.controllers.Controller import Controller
from application.models import databaseSession, Products, ProductMetaData
import random
import string
class ProductController(Controller):
    def __init__(self):
        pass

    def products(self):
        products = databaseSession.query(Products).all()
        data = {"title":"Products", "products":products}
        return self.render("dashboard/product/product", data)
    
    def add_product(self):
        if self.request().method == "POST":
            title = self.request().form["title"]
            slug = self.request().form["slug"]
            description = self.request().form["description"]
            stock = self.request().form["stock"]
            price = self.request().form["price"]

            productCode = self.generate_random_alphanumeric(8)

            productData = {"slug":slug, "user_id":1, "product_code":productCode, "is_active":1, "stocks":stock,"price": price}
            productMetaData = {"title":title,"description":description,"thumbnail":"thumbnail"}

            new_product = Products(**productData)
            new_product.product_metadata = ProductMetaData(**productMetaData)

            databaseSession.add(new_product)
            databaseSession.commit()
            databaseSession.close()

            return self.redirect("dashboard.products")
        
        data = {"title":"Add Products"}
        return self.render("dashboard/product/addProduct", data)
    
    def edit_product(self, code):
        if self.request().method == "POST":
            title = self.request().form["title"]
            slug = self.request().form["slug"]
            description = self.request().form["description"]
            stock = self.request().form["stock"]
            price = self.request().form["price"]
            edit_product = databaseSession.query(Products).filter(Products.product_code == code).first()
            if edit_product:
                edit_product.product_metadata.title = title
                edit_product.slug = slug
                edit_product.stocks = stock
                edit_product.price = price
                edit_product.product_metadata.description = description
                databaseSession.commit()
            return self.redirect("dashboard.products")
        
        edit_product = databaseSession.query(Products).filter(Products.product_code == code).first()
        data = {"title":"edit Products"+ code, "product_code": code, "product":edit_product }
        return self.render("dashboard/product/editProduct", data)
    
    def delete_product(self):
        pass

    def generate_random_alphanumeric(self,length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length)).lower()