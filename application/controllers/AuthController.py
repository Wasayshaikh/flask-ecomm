from .Controller import Controller
from application.models import ModelClasses
from application.models import databaseSession
from flask import session, jsonify


class AuthController(Controller):
    def login(self):
        request_type=super().request().method
        if request_type == "GET":
            if 'auth_user' in session:
                return super().redirect("web.index")
            else:
                data = {"title": "Login"}
                return super().render("auth/login", data)
        else:
            username = super().request().form['username']
            password = super().request().form['password']
            dataUser = databaseSession.query(ModelClasses.Users).where(ModelClasses.Users.username == username).where(ModelClasses.Users.password == password).first()
            session['auth_user'] = {"username": dataUser.username, "id":dataUser.id, "email":dataUser.email}
            print(dataUser)
            return super().redirect("web.index")

    def register(self):
        request_type = super().request().method
        if request_type == "GET":
            if 'auth_user' in session:
                return super().redirect("web.index")
            else:
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
            databaseSession.add(new_user)
            databaseSession.commit()
            databaseSession.close()
            return super().redirect("web.login")
    def logout(self):
        request_type=super().request().method
        if request_type == "GET":
            if 'auth_user' in session:
                session.pop("auth_user",None)
                return super().redirect("web.login")
            else:
                return super().redirect('web.index')
        else:
            return super().redirect('web.index')
