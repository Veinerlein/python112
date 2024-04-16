from flask import Flask, request, redirect, render_template, url_for,flash

app = Flask(__name__)

menu = [{'title': 'Main Page', 'url': "main"},
        {'title': 'Form', 'url': 'form'}]

app.config['SECRET_KEY'] = "23hr39f4v3mv343v93vj985jt89304"

@app.route('/')
@app.route('/main')
def main():
    return render_template('login.html', menu=menu, title=menu[0]['title'])


@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        if len(request.form['Username'])>2 and len(request.form['message'])>2:
            flash('Message was successfully sent',category='success')
        else:
            flash('Error to send', category='error')
    return render_template('form.html', menu=menu, title=menu[1]['title'])


@app.errorhandler(404)
def page_notf(error):
    return render_template('pagenot.html', menu=menu, title="Page not found")


if __name__ == '__main__':
    app.run(debug=True)
