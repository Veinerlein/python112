from flask import (
    Flask,
    g,
    render_template,
    url_for,
    request,
    flash,
    redirect,
    session,
    abort,
)
import sqlite3, os

# import sys
# sys.path.append('E:\pythonProject1\les\frameworks\flsk\FDataBase.py')
from FDataBase import FDataBase
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)  # усе що стосується паролів
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    current_user,
    logout_user,
)  # усе для реєстрації
from UserLogin import UserLogin  # операції із уже зареєстрованими користувачами

# в консолі # import os # os.urandom(20).hex()  # генерація випадкового ключа
# g - контекст бази даних


# configuration
DATABASE = "flsk.db"  # обовязково вказувати
DEBUG = True
SECRET_KEY = "1f67d862d68b4d496bd25eea03c0abd7fd362dd1"
MAX_CONTENT_LENGTH = 1024 * 1024  # розмір файлу

# program
app = Flask(__name__)  # створили додаток
app.config.from_object(
    __name__
)  # Метод from_object() використовується для завантаження конфігураційних налаштувань з заданого об'єкта. У цьому випадку використовується спеціальна змінна __name__, яка в Python вказує на назву поточного модуля.
# Якщо в модулі, вказаному через __name__, є змінні, що мають великі літери (наприклад, DATABASE, DEBUG, SECRET_KEY), Flask розглядає ці змінні як конфігураційні параметри і завантажує їх у app.config.

app.config.update(
    dict(DATABASE=os.path.join(app.root_path, "flsk.db"))
)  # поєдную шлях до документу\app.config це

# словкик обєкт. я його оновлюю до словника із шляхом для DATABASE

#  Цей метод приймає інший словник як аргумент і додає або оновлює ключі в основному словнику (app.config у цьому випадку) на основі переданого словника.
# dict(DATABASE=os.path.join(app.root_path, 'flsk.db')) - це створення нового словника з одним ключем DATABASE. Значенням для цього ключа є шлях до бази даних.
# os.path.join(app.root_path, 'flsk.db') - ця функція використовується для створення повного шляху до файлу бази даних. app.root_path вказує на кореневу директорію додатку Flask, а 'flsk.db' - це назва файлу бази даних. os.path.join з'єднує ці дві частини в повний шлях до файлу в системі.
# Таким чином, вираз app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db'))) додає до конфігурації
# додатку ключ DATABASE зі значенням, що вказує на розташування
# файлу бази даних. Це дозволяє легко використовувати цей шлях в інших частинах додатку, наприклад, при підключенні до бази даних.

# menu = [{'name': 'Main page', 'url': 'index'},
#         {'name': 'About us', 'url': 'about'},
#         {'name': 'Feed back', 'url': 'contact'},
#         {'name': 'Login', 'url': 'login'}]

# підключення до бази даних


login_manager = LoginManager(app)

login_manager.login_view = "login"  # через логінв'ю переходить на сторінку сам обробник логін який показує імя сайту,
# адреса іде до питального знаку. найголовніше це перехід на логін
# Для того, щоб у випадку коли гість захоче отримати доступ до даних,
# відкритих для авторизованих тільки, щоб був редірект його на форму авторизації
login_manager.login_message = (
    "Please do authorization to get the closed pages"  # підказка на зеленому фоні через
)
# категорію success
login_manager.login_message_category = "success"  # категорія


def connect_db():
    con = sqlite3.connect(app.config["DATABASE"])  # константа із конфіг
    con.row_factory = sqlite3.Row
    return con


# В контексті SQLite і бібліотеки sqlite3 у Python, row_factory є атрибутом об'єкта підключення (connection),
# який ви можете встановити для кастомізації типу об'єктів, що повертаються при виконанні запитів до бази даних.
# row_factory дозволяє вказати, яким чином мають бути представлені рядки (записи) в результатах виконання запиту.
# За замовчуванням, кожен рядок, що повертається з запиту до бази даних SQLite, представляється як кортеж (tuple).
# Це означає, що доступ до значень у кожному рядку можна отримати за індексом.
# sqlite3.Row є спеціальним класом, що використовується як row_factory, який робить рядки, що повертаються запитом,
# доступними також за назвами стовпців, а не тільки за індексом. Це робить код читабельнішим і зменшує вразливість до помилок,
# оскільки вам не потрібно пам'ятати порядок стовпців у вашому запиті, щоб отримати доступ до даних.


# створення бази даних
def create_db():
    db = connect_db()
    with app.open_resource(
        "sq_db.sql", mode="r"
    ) as f:  # метод open_resource об'єкта app (ваш Flask-додаток),
        # відкривається файл 'sq_db.sql' у режимі читання ('r'). Цей метод дозволяє легко отримати доступ до файлів,
        # що знаходяться у ресурсних директоріях вашого додатку. Файл містить SQL-команди,
        # необхідні для створення структури бази даних (таблиць, індексів, і т.д.).
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()  # якщо немає зєднання то встановити
    return g.link_db


# db = get_db()
# dbase = FDataBase(db)


@app.teardown_appcontext
def close_db(error):  # закриття зєднання
    if hasattr(g, "link_db"):
        g.link_db.close()


dbase = None  # для того щоб була видною усім обробфункціям


@app.before_request  # функція для того щоб винести в загальне бачення дві змінні у використання кожному рендеру
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.route("/index")
@app.route("/")  # прив'язує обробник до конкретного шляху
def index():
    print(url_for("index"))
    # db = get_db()
    # dbase = FDataBase(db)
    return render_template(
        "index.html",
        title="Main page",
        posts=dbase.get_all_posts(),
        menu=dbase.get_menu(),
    )


@app.route("/add_post", methods=["POST", "GET"])
@login_required
def add_post():
    # db = get_db()
    # dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = dbase.add_post(
                request.form["name"], request.form["post"], request.form["url"]
            )
            if res:
                flash("The note was added successfully", category="success")
            else:
                flash("Error to send", category="error")
        else:
            flash("Error of adding the note", category="error")

    return render_template("add_post.html", title="Add the Note", menu=dbase.get_menu())


@app.route("/del_post", methods=["POST", "GET"])
@login_required
def del_post():
    # db = get_db()
    # dbase = FDataBase(db)
    if request.method == "POST":
        res = dbase.del_post(request.form["title"])
        if res:
            flash("The note was deleted successfully", category="success")
        else:
            flash("Error to delete", category="error")
    return render_template(
        "del_post.html", title="Delete the post", menu=dbase.get_menu()
    )


@app.route("/about")
def about():
    # db = get_db()
    # dbase = FDataBase(db)
    print(url_for("about"))  # показує адресу сторінки
    return render_template("about.html", title="About us", menu=dbase.get_menu())


@app.route("/contact", methods=["POST", "GET"])
def contact():
    # db = get_db()
    # dbase = FDataBase(db)
    if request.method == "POST":
        if (
            len(request.form["usernames"]) > 2
        ):  # request form дозволяє отримати дані що є у формі по name. форма
            # отримала ці дані від введення у штмл тезі форм
            flash("Message was sent successfully", category="success")
        else:
            flash("Error to send", category="error")
        # print(request.form)  # при ключі виведе тільки дані по ключу
        # context = {
        #     'usernames': request.form['usernames'],# s показує що відповідність (одинаковість) повинна бути у 4ьох
        #     # місцях. 2 тут у цьому документі і 2 у contact.html
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template('contact.html', **context, title='Feedback', menu=menu)
    return render_template(
        "contact.html", title="Contacts and Feedback", menu=dbase.get_menu()
    )


# @app.route('/profile/<path:username>')
# def profile(username):
#     if 'userLogged' not in session or session["userLogged"] != username:
#         abort(
#             401)  # Цей статус-код зазвичай використовується для вказівки на те, що запит вимагає аутентифікації користувача.
#     return f'User: {username}'


# int: зробить тільки на інтеджер
# float: зробить тільки на дроби
# path: зробить на все і також слеш
# http://127.0.0.1:5000/profile/veinerlein

# with app.test_request_context():
#     print(url_for('about'))
#     print(url_for('index'))
#     print(url_for('profile', username='veinerlein'))


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("profile"))
    if request.method == "POST":
        user = dbase.get_user_by_email(request.form["email"])
        if user and check_password_hash(user["psw"], request.form["psw"]):
            user_login = UserLogin().create(user)

            login_user(user_login)
            return redirect(
                request.args.get("next") or url_for("profile")
            )  # дозволяє попасти після авторизації на ту
            # сторінку на яку ми пробували зайти ще до авторизації
        flash("Wrong email or password", "error")
    # if 'userLogged' in session:
    #     return redirect(url_for('profile', username=session['userLogged']))  # перевірка чи авторизований користувач
    # elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['passw'] == '123456':
    #     session['userLogged'] = request.form['username']
    #     return redirect(url_for('profile', username=session['userLogged']))

    return render_template("login.html", menu=dbase.get_menu(), title="Authorization")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if (
            len(request.form["name"]) > 1
            and len(request.form["email"]) > 4
            and len(request.form["psw"]) > 7
            and request.form["psw"] == request.form["psw2"]
        ):
            hash = generate_password_hash(request.form["psw"])
            res = dbase.add_user(request.form["name"], request.form["email"], hash)
            if res:
                flash("Registration was success", "success")
                return redirect(url_for("login"))
            else:
                flash("Error in adding to database", "error")
        else:
            print("Incorrect data")
            flash("Incorerect data", "error")
            return redirect(url_for("register"))

    return render_template("register.html", menu=dbase.get_menu(), title="Registration")


@app.errorhandler(404)
def page_not_found(error):
    # db = get_db()
    # dbase = FDataBase(db)
    return (
        render_template("page404.html", title="Page not found", menu=dbase.get_menu()),
        404,
    )


@app.route("/post/<alias>")
@login_required
def show_post(alias):
    # db = get_db()
    # dbase = FDataBase(db)
    title, post = dbase.get_post(alias)
    if not title:
        abort(404)
    return render_template("post.html", title=title, post=post, menu=dbase.get_menu())


@login_manager.user_loader  # для вказівки функції, яка буде відповідати за завантаження об'єкта користувача з деяким ідентифікатором.
# Цей механізм дозволяє Flask-Login аутентифікувати користувачів і управляти їх сеансами.
def load_user(user_id):
    print(
        "load_user"
    )  # Коли користувач входить у систему, Flask-Login зберігає унікальний ідентифікатор цього користувача в сеансі користувача,
    # а потім використовує вказану за допомогою @login_manager.user_loader функцію, щоб завантажувати об'єкт користувача за цим ідентифікатором при кожному запиті.
    # Це дозволяє додатку "запам'ятовувати" аутентифікованого користувача між запитами.
    return UserLogin().from_db(user_id, dbase)

    # @login_manager.user_loader: Цей декоратор приєднує функцію load_user до екземпляра login_manager, роблячи її "завантажувачем користувачів".
    # login_manager є екземпляром, який налаштовується при ініціалізації Flask-Login у вашому додатку.

    # load_user(user_id): Це визначення функції, що приймає user_id — ідентифікатор користувача, який потрібно завантажити.
    # print("load_user"): Просто виводить рядок "load_user" на консоль, коли функція викликається. Це може бути корисно для дебагінгу, щоб побачити,
    # коли саме виконується завантаження користувача.
    # return UserLogin().from_db(user_id, dbase): Створює новий екземпляр класу UserLogin і викликає його метод from_db,
    # передаючи ідентифікатор користувача user_id і об'єкт для взаємодії з базою даних dbase. Метод from_db повинен знайти в базі даних користувача з вказаним ідентифікатором,
    # завантажити його дані і повернути екземпляр UserLogin, який представляє цього користувача.
    # Цей екземпляр потім повертається з функції load_user і використовується Flask-Login для подальшої роботи з аутентифікованим користувачем.
    # Цей механізм є ключовим для аутентифікації та управління сеансами користувачів у додатках Flask, що використовують Flask-Login.


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", menu=dbase.get_menu(), title="Profile")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You Quited from account", "success")
    return redirect(url_for("login"))


@app.route("/userava")
@login_required
def userava():
    img = current_user.get_avatar(app)
    if not img:
        return ""
    h = app.make_response(img)  # готовий метод фласка
    h.headers["Content-Type"] = "image/png"
    return h


if __name__ == "__main__":
    app.run(debug=True)  # запускає веб сервер

# flash() - редагування повідомлення
# get_flashed_messages() - опрацювання сформованих повідомлень у документі
# дані функції використовують механізм сесій і працюють тільки із SECRET_KEY


# from flsk.first import create_db
# create_db()
# щоб побачити flsk.db потрібно оновити список проектів зліва

# щоб захистити показ паролів у базі даних
# from werkzeug.security import generate_password_hash, check_password_hash
# 1 - для створення хешу, 2 - для перевірки
# hash = generate_password_hash("1253274574683")


# check_password_hash(hash,"1253274574683") - змінна хеш містить результат функції генерації
# True - поверне якщо все ок

print(DATABASE)
