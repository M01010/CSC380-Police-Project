from flask import Blueprint, redirect, url_for, request, render_template, flash
from db_victims import DB_Victims
from db_cases import DB_Cases

victims_blueprint = Blueprint('victims', __name__, template_folder='templates', url_prefix='/victims')


@victims_blueprint.route('/')
def view_victims():
    try:
        result_set = DB_Victims.get_victims()
        return render_template('view_victims.html', victims=result_set)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return render_template('view_victims.html')


@victims_blueprint.route('/<int:victim_id>')
def view_victim(victim_id):
    try:
        result_set = DB_Victims.get_victim(victim_id)
        return render_template('view_victim.html', victim=result_set)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('victims.view_victims'))


@victims_blueprint.route('/delete/<int:victim_id>')
def delete_victim(victim_id):
    try:
        DB_Victims.delete_victim(victim_id)
        flash('Victim deleted', 'info')
        return redirect(url_for('victims.view_victims'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('victims.view_victims'))


@victims_blueprint.route('/add/', methods=['GET', 'POST'])
def add_victim():
    try:
        if request.method == 'GET':
            return render_template('add_victim.html')
        DB_Victims.add_victim(request.form)
        flash('Victim added', 'info')
        return redirect(url_for('victims.view_victims'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return render_template('add_victim.html', victim=request.form)


@victims_blueprint.route('/edit/<int:victim_id>', methods=['GET', 'POST'])
def edit_victim(victim_id):
    try:
        if request.method == 'GET':
            victim = DB_Victims.get_victim(victim_id)
            cases = DB_Cases.get_cases()
            return render_template('edit_victim.html', victim=victim, cases=cases)
        DB_Victims.edit_victim(victim_id, request.form)
        flash('Victim edited', 'info')
        return redirect(url_for('victims.view_victims'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('victims.view_victims'))
