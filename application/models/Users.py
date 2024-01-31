from application.models.db import db
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=True)
    first_name= db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    role= db.Column(db.BIGINT, nullable=False, default=0 )