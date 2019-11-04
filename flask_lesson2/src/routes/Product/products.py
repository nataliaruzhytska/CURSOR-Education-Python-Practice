import os

from flask import Blueprint, render_template, request, url_for, session
from werkzeug.utils import redirect

from src.model import ProductForm
from src.utils import get_data, add_data

products = Blueprint('products', __name__, template_folder='templates',
                     static_folder='static')


@products.route('/all_products', methods=['GET', 'POST'])
def get_all_products():
    if request.method == 'GET':
        return render_template('all_products.html', data=get_data("prod.json"))
    if request.method == 'POST':
        return redirect(url_for('all_products?price=<price>', price=request.form.get('price')))


@products.route('/product/<id>', methods=['GET', 'POST'])
def get_product(id):
    for i in get_data("prod.json"):
        if i['id'] == id:
            session[i['id']] = True
            return render_template('product.html',
                                   name=i['name'],
                                   desc=i['description'],
                                   image=i['img_name'],
                                   price=i['price'],
                                   id=i['id'])


@products.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    return render_template('add_product.html', form=form)


@products.route('/submit', methods=['POST'])
def save_product():
    f = ProductForm()

    d = {'id': f.id + request.form.get('name'),
         'name': request.form.get('name'),
         'description': request.form.get('description'),
         'price': request.form.get('price'),
         'img_name': upload_file()}

    if get_data("prod.json"):
        data = get_data("prod.json")
        data.append(d)
        add_data(data, "prod.json")
    else:
        add_data(d, "prod.json")
    return render_template('all_products.html', data=get_data("prod.json"))


@products.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        f.save(os.path.join('/home/nataliia/homework/My-Repository/flask_lesson2/src/static',
                            f.filename))
        return f.filename
