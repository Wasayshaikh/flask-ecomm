from application.controllers.Controller import Controller
from application.models import Users
from application.models import databaseSession
from flask import session
from sqlalchemy.exc import IntegrityError


class AuthController(Controller):
    def login(self):
        request_type=self.request().method
        if request_type == "GET":
            if 'auth_user' in session:
                return self.redirect("web.index")
            else:
                data = {"title": "Login"}
                return self.render("auth/login", data)
        else:
            username = self.request().form['username']
            password = self.request().form['password']
            #dataUser = databaseSession.query(ModelClasses.Users).where(ModelClasses.Users.username == username).where(ModelClasses.Users.password == password)
            dataUser = databaseSession.query(Users).filter(Users.username == username,Users.password == password).first()
            # session['auth_user'] = {"username": dataUser.username, "id":dataUser.id, "email":dataUser.email}
            if dataUser:
                return self.redirect("web.index")
            else:
                self.flash_error("Invalid credentials")
                return self.redirect("web.login")

    def register(self):
        request_type = self.request().method
        if request_type == "GET":
            if 'auth_user' in session:
                return self.redirect("web.index")
            else:
                data = {"title": "Register"}
                return self.render("auth/register", data)
        else:
            try:
                user_data = {
                    "username": self.request().form['username'],
                    "email": self.request().form['email'],
                    "password": self.request().form['password'],
                    "first_name": self.request().form['first_name'],
                    "last_name": self.request().form['last_name']
                }
                new_user = Users(**user_data)
                databaseSession.add(new_user)
                databaseSession.commit()
                databaseSession.close()
                return self.redirect("web.login")
            except IntegrityError as e:
                databaseSession.rollback()
                print("Error: Data could not be stored in the database due to integrity constraints.")
                self.flash_error("username or email already exist")
                return self.redirect('web.register')
    def logout(self):
        request_type=self.request().method
        if request_type == "GET":
            if 'auth_user' in session:
                session.pop("auth_user",None)
                return self.redirect("web.login")
            else:
                return self.redirect('web.index')
        else:
            return self.redirect('web.index')
