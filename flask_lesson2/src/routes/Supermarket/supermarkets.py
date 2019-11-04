import os

from flask import Blueprint, render_template, request, url_for, session
from werkzeug.utils import redirect

from src.model import SupermarketForm
from src.utils import get_data, add_data

supermarkets = Blueprint('supermarkets', __name__, template_folder='templates')


@supermarkets.route('/all_supermarkets', methods=['GET', 'POST'])
def get_all_supermarkets():
    if request.method == 'GET':
        return render_template('all_supermarkets.html', data=get_data("super.json"))
    if request.method == 'POST':
        return redirect(url_for('all_supermarkets?location=<location>',
                                location=request.form.get('location'), data=get_data("super.json")))


@supermarkets.route('/supermarket/<id>', methods=['GET', 'POST'])
def get_supermarket(id):
    for i in get_data("super.json"):
        if i['id'] == id:
            session[i['id']] = True
            return render_template('supermarket.html',
                                   name=i['name'],
                                   location=i['location'],
                                   image=i['img_name'],
                                   id=i['id'])


@supermarkets.route('/add_supermarket', methods=['GET', 'POST'])
def add_supermarket():
    form = SupermarketForm()
    return render_template('add_supermarket.html', form=form)


@supermarkets.route('/save', methods=['POST'])
def save_supermarket():
    form = SupermarketForm()

    s = {'id': form.id + request.form.get('name'),
         'name': request.form.get('name'),
         'location': str(request.form.get('location')).title(),
         'img_name': upload_file()}

    if get_data("super.json"):
        data = get_data("super.json")
        data.append(s)
        add_data(data, "super.json")
    else:
        add_data(s, "super.json")
    return render_template('all_supermarkets.html', data=get_data("super.json"))


@supermarkets.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        f.save(os.path.join('/home/nataliia/homework/My-Repository/flask_lesson2/src/static',
                            f.filename))
        return f.filename
