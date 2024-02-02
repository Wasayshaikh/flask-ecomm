from .Controller import Controller
from application.models import ModelClasses
from application.models import session


class AuthController(Controller):
    def login(self):
        request_type=super().request().method
        if request_type == "GET":
            data = {"title": "Login"}
            return super().render("auth/login", data)
        else:
            username = super().request().form['username']
            password = super().request().form['password']
            dataUser = session.query(ModelClasses.Users).where(ModelClasses.Users.username == username).where(ModelClasses.Users.password == password).all()
            print(dataUser)
            data = {"users" : dataUser, "title":"login"}
            return super().render("index",data)

    def register(self):
        request_type = super().request().method
        if request_type == "GET":
            data = {"title": "Register"}
            return super().render("auth/register", data)
        else:
            user_data = {
                "username": super().request().form['username'],
                "email": super().request().form['email'],
                "password": super().request().form['password'],
                "first_name": super().request().form['first_name'],
                "last_name": super().request().form['last_name']
            }
            new_user = ModelClasses.Users(**user_data)
            session.add(new_user)
            session.commit()
            session.close()
            return super().redirect("web.login")
