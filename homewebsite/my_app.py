from flask import Flask, render_template, url_for

app = Flask(__name__)



menu_punkts = [
    {'Name': 'Homepage', 'title': "HomePAGE", 'url': '/index'},
    {'Name': 'About us', 'title': "WebsiteINFO", 'url': '/about'},
    {'Name': 'Ask your question', 'title': "Popular questions", 'url': '/faq'}
]


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Main page', menu=menu_punkts)


@app.route('/about')
def about():
    return render_template('about.html', title=menu_punkts[1]['title'], menu=menu_punkts)


@app.route('/faq')
def faq():
    return render_template('faq.html', title=menu_punkts[2]['title'], menu=menu_punkts)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title='Page not found',menu=menu_punkts)

if __name__ == "__main__":
    app.run(debug=True)
