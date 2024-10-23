from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {"id": self.id, "username": self.username, "email": self.email}


with app.app_context():
    db.drop_all()
    db.create_all()
    users = [
        User(id=10, username="Bert Visser", email="bert@visser.nl"),
        User(id=11, username="Ria Visser", email="ria@visser.nl"),
        User(id=12, username="Gerrit Hiemstra", email="lekker@weer.nl"),
    ]
    db.session.add_all(users)
    db.session.commit()


@app.route("/user-by-id/<int:id>")
def user_by_id(id):
    user = db.get_or_404(User, id)
    return user.json()


# create a test route
@app.route("/users", methods=["GET"])
def test():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return [user.json() for user in users]
