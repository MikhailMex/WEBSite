from flask import Flask, render_template
from flask import Blueprint

app = Flask(__name__)

site1 = Blueprint('site1', __name__, template_folder='templates', static_folder='static')
site2 = Blueprint('site2', __name__, template_folder='templates', static_folder='static')
site3 = Blueprint('site3', __name__, template_folder='templates', static_folder='static')
site4 = Blueprint('site4', __name__, template_folder='templates', static_folder='static')
site5 = Blueprint('site5', __name__, template_folder='templates', static_folder='static')
site6 = Blueprint('site6', __name__, template_folder='templates', static_folder='static')
site7 = Blueprint('site7', __name__, template_folder='templates', static_folder='static')
site8 = Blueprint('site8', __name__, template_folder='templates', static_folder='static')
site9 = Blueprint('site9', __name__, template_folder='templates', static_folder='static')


@site1.route('/fact')
def show_site1():
    return render_template('fact.html')


@site2.route('/foto')
def show_site2():
    return render_template('foto.html')


@site3.route('/geo')
def show_site3():
    return render_template('geo.html')


@site4.route('/history')
def show_site4():
    return render_template('history.html')


@site5.route('/index')
def show_site5():
    return render_template('index.html')


@site6.route('/karta')
def show_site6():
    return render_template('Karta.html')


@site7.route('/ob_avtore')
def show_site7():
    return render_template('Ob_avtore.html')


@site8.route('/simvolika')
def show_site8():
    return render_template('Simvolika.html')


@site9.route('/spisok')
def show_site8():
    return render_template('spisok.html')


app.register_blueprint(site1)
app.register_blueprint(site2)
app.register_blueprint(site3)
app.register_blueprint(site4)
app.register_blueprint(site5)
app.register_blueprint(site6)
app.register_blueprint(site7)
app.register_blueprint(site8)
app.register_blueprint(site9)

if __name__ == '__main__':
    app.run()