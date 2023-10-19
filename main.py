from datetime import datetime

from flask import Flask, render_template, flash, redirect, url_for, request
from psycopg2.extras import RealDictCursor

from tests import tests
from database import Database

app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(tests)


@app.route('/')
def home():
    return render_template('home.html', title='home')


@app.route('/about-supabase')
def about_supabase():
    start = datetime.now()
    connection = None
    cursor = None
    try:
        connection = Database.connect_supabase()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute('select * from test')
        result_set = cursor.fetchall()
        diff = datetime.now() - start
        return render_template('about.html', tests=result_set, time=diff.total_seconds())
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return render_template('about.html')
    finally:
        try:
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app.run(debug=True)
