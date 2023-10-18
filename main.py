from flask import Flask, render_template
import psycopg2
from psycopg2.extras import RealDictCursor

from config import Config

app = Flask(__name__)

posts = [
    {
        'author': '11',
        'name': 'dd',
    },
    {
        'author': '23',
        'name': 'ertu',
    },
    {
        'author': '55',
        'name': 'fgh',
    }
]


@app.route('/home')
@app.route('/')
def hello():
    return render_template('home.html', title='home', posts=posts)


def connect():
    con = psycopg2.connect(
        database=Config.database,
        host=Config.host,
        user=Config.user,
        password=Config.password,
        port=Config.port
    )
    return con


@app.route('/about')
def about():
    try:
        connection = connect()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute('select * from test')
        result_set = cursor.fetchall()
        return render_template('about.html', tests=result_set)
    except Exception as e:
        print(e)
        return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
