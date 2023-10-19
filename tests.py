from datetime import datetime

from flask import Blueprint, redirect, url_for, request, render_template, flash

from database import Database

tests = Blueprint('tests', __name__, template_folder='templates')


@tests.route('/delete/<test_id>')
def delete_test(test_id):
    try:
        Database.Test.delete_test(test_id)
        return redirect(url_for('tests.about_sqlite'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return redirect(url_for('tests.about_sqlite'))


@tests.route('/add/', methods=['GET', 'POST'])
def add_test():
    if request.method == 'GET':
        return render_template('add_test.html')
    else:
        try:
            Database.Test.add_test(request.form)
            return redirect(url_for('tests.about_sqlite'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')  # send the alert
            return render_template('add_test.html', test=request.form)


@tests.route('/edit/<test_id>', methods=['GET', 'POST'])
def edit_test(test_id):
    try:
        test = Database.Test.get_test(test_id)
        if request.method == 'POST':
            Database.Test.edit_test(test_id, request.form)
            return redirect(url_for('tests.about_sqlite'))
        return render_template('edit_test.html', test=test)
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return render_template('edit_test.html', test=test)


@tests.route('/about-sqlite')
def about_sqlite():
    start = datetime.now()
    try:
        result_set = Database.Test.get_tests()
        diff = datetime.now() - start
        return render_template('about.html', tests=result_set, time=diff.total_seconds())
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return render_template('about.html')
