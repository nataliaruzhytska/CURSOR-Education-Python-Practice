from datetime import timedelta

from flask import Flask, render_template
from src.routes.Product.products import products
from src.routes.Supermarket.supermarkets import supermarkets

app = Flask(__name__, template_folder='templates')

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


app.register_blueprint(products)
app.register_blueprint(supermarkets)


app.config['SESSION_TYPE'] = 'filesystem'
app.permanent_session_lifetime = timedelta(seconds=10)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404_page.html'), 404


@app.route('/')
@app.route('/home')
def get_home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
