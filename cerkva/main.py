import sqlite3
from DATA import DATA
from flask import Flask, render_template, session, url_for, g, request, flash, redirect
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_required
from UserLoader import UserLoader

DATABASE = "cerkva.db"  # name
SECRET_KEY = ""
DEBAG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "cerkva.db")))

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Для того щоб отримати благословення на відвідування цих сторінок зареєструйтесь будь ласка"
login_manager.login_message_category = "success"


def connect_db():
    con = sqlite3.connect(app.config["DATABASE"])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("SQL_Cerkva.sql", "r") as f:
        db.cursor().execute(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


dbase = None


@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = DATA(db)


@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.html", menu=dbase.get_menu(), title="Вас вітає духовне царство"
    )


@app.route("/poslugi")
def poslugi():
    return render_template(
        "poslugi.html",
        menu=dbase.get_menu(),
        title="Тут ви можете придбати спасіння для своєї душі",
    )


@app.route("/addprod", methods=["POST", "GET"])
def add_product():
    if request.method == "POST":
        res = dbase.add_prod(
            request.form["product"], request.form["price"], request.form["image"]
        )
    return render_template(
        "addprod.html", menu=dbase.get_menu(), title="Чисто додати якусь нову штучку"
    )


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        menu=dbase.get_menu(),
        title="Якщо вам хочеться подякувати нам за ваше спасіння, то це тут",
    )


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        if (
            len(request.form["name"]) < 2
            and len(request.form["nickname"]) < 2
            and len(request.form["email"]) < 4
            and request.form["psw"] != request.form["psw2"]
        ):
            print("Введені дані некоректні")
            flash("Некоректні дані у полях вводу", "error")
            return redirect(url_for("login"))
        hash = generate_password_hash(request.form["psw"])

        try:
            res = dbase.add_user(
                request.form["name"],
                request.form["nickname"],
                request.form["email"],
                hash,
            )
            print("Реєстрація пройшла успішно", "success")
            return redirect(url_for("login"))
        except sqlite3.Error as e:
            print("Помилка контакту із базою даних" + str(e))
            return redirect(url_for("register"))

    return render_template(
        "register.html",
        menu=dbase.get_menu(),
        title="Станьте нашим постійним клієнтом та отримайте +1 до карми",
    )


@login_manager.user_loader
def load_user(user_id):
    print("тут Працює load_user")
    return UserLoader.from_db(user_id, dbase)


@app.route("/buy")
def buy():
    return render_template(
        "buy.html",
        menu=dbase.get_menu(),
        title="Купуючи нашу продукцію ви отримуєте наше благословення",
    )


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template(
        "login.html", menu=dbase.get_menu(), title="Увійдіть у ворота спокою свого"
    )


if __name__ == "__main__":
    app.run(debug=True)
