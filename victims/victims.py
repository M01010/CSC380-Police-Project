from flask import Blueprint, redirect, url_for, request, render_template, flash

from database import Database

victims = Blueprint('victims', __name__, template_folder='templates', url_prefix='/victims')





@victims.route('/')
def view_victims():
    try:
        result_set = Database.Victims.get_victims()
        return render_template('view_victims.html', victims=result_set)
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return render_template('view_victims.html')

@victims.route('/<victim_id>')
def view_victim(victim_id):
    try:
        result_set = Database.Victims.get_victim(victim_id)
        return render_template('view_victim.html', victim=result_set)
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return redirect(url_for('victims.view_victims'))

@victims.route('/delete/<victim_id>')
def delete_victim(victim_id):
    try:
        Database.Victims.delete_victim(victim_id)
        flash('victim deleted', 'info')
        return redirect(url_for('victims.view_victims'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return redirect(url_for('victims.view_victims'))


@victims.route('/add/', methods=['GET', 'POST'])
def add_victim():
    if request.method == 'GET':
        return render_template('add_victim.html')
    try:
        Database.Victims.add_victim(request.form)
        flash('victim added', 'info')
        return redirect(url_for('victims.view_victims'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return render_template('add_victim.html', victim=request.form)


@victims.route('/edit/<victim_id>', methods=['GET', 'POST'])
def edit_victim(victim_id):
    try:
        test = Database.Victims.get_victim(victim_id)
        if request.method == 'POST':
            Database.Victims.edit_victim(victim_id, request.form)
            flash('victim edited', 'info')
            return redirect(url_for('victims.view_victims'))
        return render_template('edit_victim.html', victim=test)
    except Exception as e:
        flash(f'Error: {e}', 'danger')  # send the alert
        return redirect(url_for('victims.view_victims'))
