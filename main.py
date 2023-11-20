from flask import Flask, render_template
from victims.victims import victims
from officers import officers
from cases import cases



app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(victims, url_prefix='/victims')
app.register_blueprint(officers, url_prefix='/officers')
app.register_blueprint(cases, url_prefix='/cases')



@app.route('/')
def home():
    return render_template('home.html', title='home')


if __name__ == '__main__':
    app.run(debug=True)
