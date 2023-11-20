from flask import Blueprint, request, render_template, redirect, url_for, flash
from database import Database

officers = Blueprint('officers', __name__, template_folder='templates', url_prefix='/officers')

@officers.route('/')
def view_officers():
    try:
        officer_list = Database.Officers.get_officers()
        return render_template('view_officers.html', officers=officer_list)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return render_template('view_officers.html')

@officers.route('/<int:officer_id>')
def view_officer(officer_id):
    try:
        officer = Database.Officers.get_officer(officer_id)
        if officer:
            return render_template('view_officer.html', officer=officer)
        else:
            flash('Officer not found.', 'danger')
            return redirect(url_for('officers.view_officers'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('officers.view_officers'))

@officers.route('/add/', methods=['GET', 'POST'])
def add_officer():
    if request.method == 'POST':
        officer_id = request.form.get('officer_id')
        badge_number = request.form.get('badge_number')


        # Validate that officer_id and badge_number are numeric
        if not officer_id.isdigit() :#or not badge_number.isdigit():
            flash('Invalid Officer ID. Please enter a numeric value.', 'danger')
            return render_template('add_officer.html', officer=request.form)

        try:
            officer_data = {
                'officer_id': officer_id,
                'name': request.form['name'],
                'badge_number': badge_number,
                'rank': request.form['rank'],
                'date_of_birth': request.form['date_of_birth']
            }
            Database.Officers.add_officer(officer_data)
            flash('Officer added successfully!', 'info')
            return redirect(url_for('officers.view_officers'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')

    return render_template('add_officer.html')

@officers.route('/edit/<int:officer_id>', methods=['GET', 'POST'])
def edit_officer(officer_id):
    try:
        if request.method == 'POST':
            officer_data = {
                'name': request.form['name'],
                'badge_number': request.form['badge_number'],
                'rank': request.form['rank'],
                'date_of_birth': request.form['date_of_birth']
            }
            Database.Officers.edit_officer(officer_id, officer_data)
            flash('Officer updated successfully!', 'info')
            return redirect(url_for('officers.view_officers'))

        officer = Database.Officers.get_officer(officer_id)
        return render_template('edit_officer.html', officer=officer)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('officers.view_officers'))

@officers.route('/delete/<int:officer_id>')
def delete_officer(officer_id):
    try:
        Database.Officers.delete_officer(officer_id)
        flash('Officer deleted successfully!', 'info')
    except Exception as e:
        flash(f'Error: {e}', 'danger')
    return redirect(url_for('officers.view_officers'))
