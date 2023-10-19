from datetime import datetime

from flask import Flask, render_template, flash, redirect, url_for, request
from psycopg2.extras import RealDictCursor
from database import Database

app = Flask(__name__)
app.secret_key = '123'


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


@app.route('/tests/delete/<test_id>')
def delete_test(test_id):
    connection = None
    cursor = None
    try:
        connection = Database.connect_sqlite()
        cursor = connection.cursor()
        cursor.execute(f'delete from test where id={test_id}')
        connection.commit()
        return redirect(url_for('about_sqlite'))
    except Exception as e:
        print(e)
        flash(f'Error: {e}', 'danger')  # send the alert
        return redirect(url_for('about_sqlite'))
    finally:
        try:
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)


@app.route('/tests/add/', methods=['GET', 'POST'])
def add_test():
    if request.method == 'POST':
        test = {
            'id': request.form['id'],
            'name': request.form['name']
        }
        connection = None
        cursor = None
        try:
            print(test)
            connection = Database.connect_sqlite()
            cursor = connection.cursor()
            cursor.execute(f'insert into test values ("{test["id"]}", "{test["name"]}")')
            connection.commit()
            return redirect(url_for('about_sqlite'))
        except Exception as e:
            print(e)
            flash(f'Error: {e}', 'danger')  # send the alert
            return render_template('add_test.html', test=test)
        finally:
            try:
                cursor.close()
                connection.close()
            except Exception as e:
                print(e)

    return render_template('add_test.html')

@app.route('/tests/edit/<test_id>', methods=['GET', 'POST'])
def edit_test(test_id):
    connection = None
    cursor = None
    test = None
    try:
        connection = Database.connect_sqlite()
        cursor = connection.cursor()
        cursor.execute(f'select * from test where id={test_id}')
        test = cursor.fetchone()
        if request.method == 'POST':
            cursor.execute(f'update test set id ={request.form["id"]}, name="{request.form["name"]}" where id={test_id}')
            connection.commit()
            return redirect(url_for('about_sqlite'))
        return render_template('edit_test.html', test=test)
    except Exception as e:
        print(e)
        flash(f'Error: {e}', 'danger')  # send the alert
        return render_template('edit_test.html', test=test)
    finally:
        try:
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)


@app.route('/about-sqlite')
def about_sqlite():
    start = datetime.now()
    connection = None
    cursor = None
    try:
        connection = Database.connect_sqlite()
        cursor = connection.cursor()
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
