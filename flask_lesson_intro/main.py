from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", title="Home")


@app.route('/<item>')
def get_item_page(item):
    for i in get_data():
        if i['title'] == item:
            return render_template("item.html",
                                   title=i['title'],
                                   image=i['img'],
                                   text=i['text'],
                                   count=len(i['text'].split()),
                                   data=get_data())
    else:
        return render_template("404_page.html")


@app.route('/author_page')
def get_author_page():
    return render_template('/author_page.html')


if __name__ == "__main__":
    app.run(debug=True)
