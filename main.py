from flask import Flask, render_template
from victims.victims import victims_blueprint
from officers.officers import officers_blueprint
from cases.cases import cases_blueprint
from suspects.suspects import suspects_blueprint

app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(suspects_blueprint,url_prefix='/suspects')
app.register_blueprint(victims_blueprint, url_prefix='/victims')
app.register_blueprint(officers_blueprint, url_prefix='/officers')
app.register_blueprint(cases_blueprint, url_prefix='/cases')


@app.route('/')
def home():
    return render_template('home.html', title='home')


if __name__ == '__main__':
    app.run(debug=True)
