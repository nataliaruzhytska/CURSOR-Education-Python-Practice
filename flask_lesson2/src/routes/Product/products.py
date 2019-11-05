import os

from flask import Blueprint, render_template, request, url_for, session
from werkzeug.utils import redirect

from src.model import ProductForm
from src.utils import get_data, add_data

products = Blueprint('products', __name__, template_folder='templates',
                     static_folder='static', static_url_path='/routes/Product/static')

product_list = "prod.json"
products_upload = '/home/nataliia/homework/My-Repository/flask_lesson2/src/routes/Product/static'


@products.route('/all_products', methods=['GET'])
def get_all_products():
    return render_template('all_products.html', data=get_data(product_list))


@products.route('/all_products', methods=['POST'])
def get_some_products():
    return redirect(url_for('all_products?price=<price>', price=request.form.get('price')))


@products.route('/product/<prod_id>', methods=['GET', 'POST'])
def get_product(prod_id):
    for i in get_data(product_list):
        if i['id'] == prod_id:
            session[i['id']] = True
            return render_template('product.html',
                                   name=i['name'],
                                   desc=i['description'],
                                   image=i['img_name'],
                                   price=i['price'],
                                   prod_id=i['id'])


@products.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    return render_template('add_product.html', form=form)


@products.route('/submit', methods=['POST'])
def save_product():
    f = ProductForm()

    d = {'id': f.id,
         'name': request.form.get('name'),
         'description': request.form.get('description'),
         'price': request.form.get('price'),
         'img_name': upload_file()}

    if get_data(product_list):
        data = get_data(product_list)
        data.append(d)
        add_data(data, product_list)
    else:
        add_data(d, product_list)
    return render_template('all_products.html', data=get_data(product_list))


@products.route('/upload', methods=['POST'])
def upload_file():
    if request.files['image']:
        f = request.files['image']
        f.save(os.path.join(products_upload, f.filename))
        return f.filename
    else:
        return 'no_image.png'
