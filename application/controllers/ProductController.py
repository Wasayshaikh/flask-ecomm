from application.controllers.Controller import Controller
from application.models import databaseSession, Products, ProductMetaData
from werkzeug.utils import secure_filename
import random
import string
import os
from application.helper import check_auth
class ProductController(Controller):
    def __init__(self):
        pass

    @check_auth
    def products(self):
        products = databaseSession.query(Products).all()
        data = {"title":"Products", "products":products}
        return self.render("dashboard/product/product", data)
    
    @check_auth
    def add_product(self):
        if self.request().method == "POST":
            upload_file_path = self.upload_file()
            if "status" not in upload_file_path:
                # return render_template('dashboard/pages/posts/create_post.html')
                upload_file_path['path'] = None

            title = self.request().form["title"]
            slug = self.request().form["slug"]
            description = self.request().form["description"]
            stock = self.request().form["stock"]
            price = self.request().form["price"]

            productCode = self.generate_random_alphanumeric(8)

            productData = {"slug":slug, "user_id":1, "product_code":productCode, "is_active":1, "stocks":stock,"price": price}
            productMetaData = {"title":title,"description":description,"thumbnail":upload_file_path['path']}

            new_product = Products(**productData)
            new_product.product_metadata = ProductMetaData(**productMetaData)

            databaseSession.add(new_product)
            databaseSession.commit()
            databaseSession.close()

            return self.redirect("dashboard.products")
        
        data = {"title":"Add Products"}
        return self.render("dashboard/product/addProduct", data)
    
    @check_auth
    def edit_product(self, code):
        if self.request().method == "POST":
            upload_file_path = self.upload_file()
            title = self.request().form["title"]
            slug = self.request().form["slug"]
            description = self.request().form["description"]
            stock = self.request().form["stock"]
            price = self.request().form["price"]

            edit_product = databaseSession.query(Products).filter(Products.product_code == code).first()
            if "status" not in upload_file_path:
                # return render_template('dashboard/pages/posts/create_post.html')
                upload_file_path["path"] =  edit_product.product_metadata.thumbnail

            if edit_product:
                edit_product.product_metadata.title = title
                edit_product.slug = slug
                edit_product.stocks = stock
                edit_product.price = price
                edit_product.product_metadata.description = description
                edit_product.product_metadata.thumbnail =upload_file_path["path"]
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
    
    def upload_file(self):
        UPLOAD_DIR ="static/img/uploads/"
        if 'image' not in self.request().files:
            return False
        
        file = self.request().files['image']

        if file.filename == '':
            return False
        else:
            filename = secure_filename(file.filename)
            new_filename = self.generate_random_alphanumeric(10)

            _, file_extension = os.path.splitext(filename)

            new_filename_with_extension = new_filename + file_extension

            original_path = os.path.join(UPLOAD_DIR, filename)
            file.save(original_path)

            new_path = os.path.join(UPLOAD_DIR, new_filename_with_extension)
            os.rename(original_path, new_path)  #

            path = os.path.join('img/uploads/', new_filename_with_extension)
            return {"status" :True, "path" : path}