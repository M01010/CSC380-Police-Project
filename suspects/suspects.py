from flask import Blueprint, redirect, url_for, request, render_template, flash
from db_suspects import DB_Suspects
from db_cases import DB_Cases
from constants import Constants

suspects_blueprint = Blueprint('suspects', __name__, template_folder='templates', url_prefix='/suspects')


@suspects_blueprint.route('/', methods=['GET', 'POST'])
def view_suspects():
    try:
        if request.method == 'GET':
            result_set = DB_Suspects.get_suspects()
            return render_template('view_suspects.html', suspects=result_set)
        result_set = DB_Suspects.get_suspects_by_name(request.form['search'])
        return render_template('view_suspects.html', suspects=result_set)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return render_template('view_suspects.html')


@suspects_blueprint.route('/<int:suspect_id>')
def view_suspect(suspect_id):
    try:
        result_set = DB_Suspects.get_suspect(suspect_id)
        cases = DB_Cases.get_cases_for_suspect(suspect_id)
        return render_template('view_suspect.html', suspect=result_set, cases=cases)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('suspects.view_suspects'))


@suspects_blueprint.route('/delete/<int:suspect_id>')
def delete_suspect(suspect_id):
    try:
        DB_Suspects.delete_suspect(suspect_id)
        flash('suspect deleted', 'info')
        return redirect(url_for('suspect.view_suspects'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('suspects.view_suspects'))


@suspects_blueprint.route('/add/', methods=['GET', 'POST'])
def add_suspect():
    try:
        if request.method == 'GET':
            return render_template('add_suspect.html', constants=Constants)
        DB_Suspects.add_suspect(request.form)
        flash('Suspect added', 'info')
        return redirect(url_for('suspects.view_suspects'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return render_template('add_suspect.html', suspect=request.form,
                               constants=Constants)


@suspects_blueprint.route('/edit/<int:suspect_id>', methods=['GET', 'POST'])
def edit_suspect(suspect_id):
    try:
        if request.method == 'GET':
            suspect = DB_Suspects.get_suspect(suspect_id)
            cases = DB_Cases.get_cases()
            return render_template('edit_suspect.html', suspect=suspect, cases=cases,
                                   constants=Constants)
        DB_Suspects.edit_suspect(suspect_id, request.form)
        flash('suspect edited', 'info')
        return redirect(url_for('suspect.view_suspects'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('suspect.view_suspects'))
