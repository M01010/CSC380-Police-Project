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


@app.route('/about')
def about():
    db = psycopg2.connect(
        database=Config.database,
        host=Config.host,
        user=Config.user,
        password=Config.password,
        port=Config.port
    )
    cursor = db.cursor(
        cursor_factory=RealDictCursor
    )
    cursor.execute(
        'select * from test'
    )
    result_set = cursor.fetchall()
    for a in result_set:
        print(f"id: {a['id']}, name: {a['name']}")
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
