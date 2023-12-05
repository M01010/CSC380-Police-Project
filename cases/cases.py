from flask import Blueprint, request, render_template, redirect, url_for, flash
from db_cases import DB_Cases
from db_officers import DB_Officers
from db_victims import DB_Victims
from db_suspects import DB_Suspects
from constants import Constants

cases_blueprint = Blueprint('cases', __name__, template_folder='templates', url_prefix='/cases')


@cases_blueprint.route('/')
def view_cases():
    try:
        all_cases = DB_Cases.get_cases()
        return render_template('view_cases.html', cases=all_cases)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('home'))


@cases_blueprint.route('/<int:case_id>')
def view_case(case_id):
    try:
        case = DB_Cases.get_case(case_id)
        suspects = DB_Suspects.get_suspects_by_case(case_id)
        victims = DB_Victims.get_victims_by_case(case_id)
        return render_template('view_case.html', case=case, victims=victims, suspects=suspects)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_cases'))


@cases_blueprint.route('/delete/<int:case_id>')
def delete_case(case_id):
    try:
        DB_Cases.delete_case(case_id)
        flash("Case deleted successfully!", "info")
        return redirect(url_for('cases.view_cases'))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_cases'))


@cases_blueprint.route('/add', methods=['GET', 'POST'])
def add_case():
    try:
        if request.method == 'GET':
            officers = DB_Officers.get_officers()
            return render_template('add_case.html', officers=officers,
                                   constants=Constants)
        DB_Cases.add_case(request.form)
        flash("Case added successfully!", "info")
        return redirect(url_for('cases.view_case', case_id=request.form['case_id']))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_cases'))


@cases_blueprint.route('/edit/<int:case_id>', methods=['GET', 'POST'])
def edit_case(case_id):
    try:
        if request.method == 'GET':
            case = DB_Cases.get_case(case_id)
            officer = DB_Officers.get_officer(case['OFFICER_officer_id'])
            officers = DB_Officers.get_officers()
            return render_template('edit_case.html', case=case, officer=officer, officers=officers,
                                   constants=Constants)
        DB_Cases.edit_case(case_id, request.form)
        flash("Case updated successfully!", "info")
        return redirect(url_for('cases.view_case', case_id=case_id))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_cases'))


@cases_blueprint.post('/edit/<int:case_id>/victims/<int:victim_id>/<int:delete>')
def edit_case_victims_edit(case_id, delete=False, victim_id=0):
    try:
        if delete:
            DB_Victims.delete_victim_from_case(victim_id, case_id)
            flash("victim deleted successfully!", "info")
        else:
            DB_Victims.add_victim_to_case(victim_id, case_id)
            flash("victim added successfully!", "info")
        victims = DB_Victims.get_victims_by_case(case_id)
        all_victims = DB_Victims.get_victims_not_in_case(case_id)
        return render_template('edit_case_victims.html', case_id=case_id, victims=victims, all_victims=all_victims)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_case', case_id=case_id))


@cases_blueprint.get('/edit/<int:case_id>/victims')
def edit_case_victims(case_id):
    try:
        victims = DB_Victims.get_victims_by_case(case_id)
        all_victims = DB_Victims.get_victims_not_in_case(case_id)
        return render_template('edit_case_victims.html', case_id=case_id, victims=victims, all_victims=all_victims)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_case', case_id=case_id))


@cases_blueprint.post('/edit/<int:case_id>/suspects/<int:suspect_id>/<int:delete>')
def edit_case_suspects_edit(case_id, delete=False, suspect_id=0):
    try:
        if delete:
            DB_Suspects.delete_suspect_from_case(suspect_id, case_id)
            flash("suspect deleted successfully!", "info")
        else:
            DB_Suspects.add_suspect_to_case(suspect_id, case_id)
            flash("suspect added successfully!", "info")
        suspects = DB_Suspects.get_suspects_by_case(case_id)
        all_suspects = DB_Suspects.get_suspects_not_in_case(case_id)
        return render_template('edit_case_suspects.html', case_id=case_id, suspects=suspects, all_suspects=all_suspects)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_case', case_id=case_id))


@cases_blueprint.get('/edit/<int:case_id>/suspects')
def edit_case_suspects(case_id):
    try:
        suspects = DB_Suspects.get_suspects_by_case(case_id)
        all_suspects = DB_Suspects.get_suspects_not_in_case(case_id)
        return render_template('edit_case_suspects.html', case_id=case_id, suspects=suspects, all_suspects=all_suspects)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_case', case_id=case_id))
