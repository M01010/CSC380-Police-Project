from flask import Flask, render_template, flash
from psycopg2.extras import RealDictCursor
from database import Database

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def hello():
    return render_template('home.html', title='home')


@app.route('/about-supabase')
def about_supabase():
    connection = None
    cursor = None
    try:
        connection = Database.connect_supabase()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute('select * from test')
        result_set = cursor.fetchall()
        return render_template('about.html', tests=result_set)
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return render_template('about.html')
    finally:
        try:
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)


@app.route('/about-sqlite')
def about_sqlite():
    connection = None
    cursor = None
    try:
        connection = Database.connect_sqlite()
        cursor = connection.cursor()
        cursor.execute('select * from test')
        result_set = cursor.fetchall()
        return render_template('about.html', tests=result_set)
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
