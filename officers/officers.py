from flask import Blueprint, request, render_template, redirect, url_for, flash
from db_officers import DB_Officers

officers_blueprint = Blueprint('officers', __name__, template_folder='templates', url_prefix='/officers')


@officers_blueprint.route('/')
def view_officers():
    try:
        officer_list = DB_Officers.get_officers()
        return render_template('view_officers.html', officers=officer_list)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return render_template('view_officers.html')


@officers_blueprint.route('/<int:officer_id>')
def view_officer(officer_id):
    try:
        officer = DB_Officers.get_officer(officer_id)
        return render_template('view_officer.html', officer=officer)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('officers.view_officers'))


@officers_blueprint.route('/delete/<int:officer_id>')
def delete_officer(officer_id):
    try:
        DB_Officers.delete_officer(officer_id)
        flash('Officer deleted successfully!', 'info')
    except Exception as e:
        flash(f'Error: {e}', 'danger')
    return redirect(url_for('officers.view_officers'))


@officers_blueprint.route('/add/', methods=['GET', 'POST'])
def add_officer():
    try:
        if request.method == 'GET':
            return render_template('add_officer.html')
        DB_Officers.add_officer(request.form)
        flash('Officer added successfully!', 'info')
        return redirect(url_for('officers.view_officers'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('officers.view_officers'))


@officers_blueprint.route('/edit/<int:officer_id>', methods=['GET', 'POST'])
def edit_officer(officer_id):
    try:
        if request.method == 'GET':
            officer = DB_Officers.get_officer(officer_id)
            return render_template('edit_officer.html', officer=officer)
        DB_Officers.edit_officer(officer_id, request.form)
        flash('Officer updated successfully!', 'info')
        return redirect(url_for('officers.view_officers'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('officers.view_officers'))
