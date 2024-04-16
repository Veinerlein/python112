import os.path
import sqlite3
from BaseD import Base

from flask import Flask, g, render_template, abort, session, request, flash, url_for

app = Flask(__name__)
SECRET_KEY = '50ffb0554967aec1f738e8972dc5099c0acddb95'
DEBUG = True
DATABASE = 'menu.db'

app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'menu.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('db_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


# from flsk2 import create__db
# create_db()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
@app.route('/main')
def main():
    db = connect_db()
    dbase = Base(db)
    return render_template('main.html', menu=dbase.get_menu(), title='Main')


@app.route('/login', methods=['POST', 'GET'])
def login():
    db = connect_db()
    dbase = Base(db)
    return render_template('login.html', menu=dbase.get_menu(), title='Login')


@app.route('/profile/<path:username>')
def profile(username):
    db = connect_db()
    dbase = Base(db)
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return render_template('profile.html', menu=dbase.get_menu(), title='Profile')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Page not Found')  # ,404  ставити не обовязково в наш час


@app.route('/add_menu', methods=['POST', 'GET'])
def add_menu():
    db = get_db()
    dbase = Base(db)
    if request.method == 'POST':
        if request.form['menu_name'] and request.form['url']:
            res = dbase.add_menu(request.form['menu_name'], request.form["url"])
            if res:
                flash('The new menu was added successfully', category='success')
            else:
                flash('Error to add', category='error')
        else:
            flash('Error', category='error')
    return render_template('add_menu.html', title='Add the menu', menu=dbase.get_menu())


@app.route('/del_menu', methods=['POST', 'GET'])
def del_menu():
    db = get_db()
    dbase = Base(db)
    if request.method == 'POST':
        if request.form['menu_name']:
            res = dbase.del_menu(request.form['menu_name'])
            if res:
                flash('The new menu was deleted successfully', category='success')
            else:
                flash('Error to delete', category='error')
        else:
            flash('Error', category='error')
    return render_template('del_menu.html', title='del the menu', menu=dbase.get_menu())


if __name__ == "__main__":
    app.run(debug=True)
