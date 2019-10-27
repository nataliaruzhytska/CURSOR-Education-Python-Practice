from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/Alarm_clock')
def get_alarm_clock():
    return render_template('alarm_clock.html', data=get_data())


@app.route('/Headphones')
def get_headphones():
    return render_template('headphones.html', data=get_data())


@app.route('/iPod')
def get_ipod():
    return render_template('ipod.html', data=get_data())


@app.route('/Calculator')
def get_calculator():
    return render_template('calculator.html', data=get_data())


@app.route('/Coffeemaker')
def get_coffeemaker():
    return render_template('coffeemaker.html', data=get_data())


@app.route('/Battery_charger')
def get_battery_charger():
    return render_template('battery_charger.html', data=get_data())


@app.route('/author_page')
def get_author_page():
    return render_template('/author_page.html')


if __name__ == "__main__":
    app.run(debug=True)
