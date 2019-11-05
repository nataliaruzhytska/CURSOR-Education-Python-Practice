import os

from flask import Blueprint, render_template, request, url_for, session
from werkzeug.utils import redirect


from src.model import SupermarketForm
from src.utils import get_data, add_data

supermarkets = Blueprint('supermarkets', __name__, template_folder='templates',
                         static_folder='static', static_url_path='/routes/Supermarket/static')

SUPERMARKET_LIST = "super.json"


@supermarkets.route('/all_supermarkets', methods=['GET'])
def get_all_supermarkets():
    return render_template('all_supermarkets.html', data=get_data(SUPERMARKET_LIST))


@supermarkets.route('/all_supermarkets', methods=['POST'])
def get_some_supermarkets():
    return redirect(url_for('all_supermarkets?location=<location>',
                            location=request.form.get('location'), data=get_data(SUPERMARKET_LIST)))


@supermarkets.route('/supermarket/<s_id>', methods=['GET', 'POST'])
def get_supermarket(s_id):
    for i in get_data(SUPERMARKET_LIST):
        if i['id'] == s_id:
            session[i['id']] = True
            return render_template('supermarket.html',
                                   name=i['name'],
                                   location=i['location'],
                                   image=i['img_name'],
                                   id=i['id'])
    else:
        return render_template('404_page.html')


@supermarkets.route('/add_supermarket', methods=['GET', 'POST'])
def add_supermarket():
    form = SupermarketForm()
    return render_template('add_supermarket.html', form=form)


@supermarkets.route('/save', methods=['POST'])
def save_supermarket():
    form = SupermarketForm()

    s = {'id': form.id,
         'name': request.form.get('name'),
         'location': str(request.form.get('location')).title(),
         'img_name': upload_file()}

    if get_data(SUPERMARKET_LIST):
        data = get_data(SUPERMARKET_LIST)
        data.append(s)
        add_data(data, SUPERMARKET_LIST)
    else:
        add_data(s, SUPERMARKET_LIST)
    return render_template('all_supermarkets.html', data=get_data(SUPERMARKET_LIST))


@supermarkets.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.files['image']:
        f = request.files['image']
        f.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', f.filename))
        return f.filename
    else:
        return 'no_image.png'
