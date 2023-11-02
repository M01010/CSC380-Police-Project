from flask import Flask, render_template
from victims.victims import victims

app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(victims)


@app.route('/')
def home():
    return render_template('home.html', title='home')


if __name__ == '__main__':
    app.run(debug=True)
