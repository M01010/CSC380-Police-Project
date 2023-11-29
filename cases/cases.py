from flask import Blueprint, request, render_template, redirect, url_for, flash
from db_cases import DB_Cases
from db_officers import DB_Officers
from db_victims import DB_Victims

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
        victims = DB_Victims.get_victims_by_case(case_id)
        return render_template('view_case.html', case=case, victims=victims)
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
            return render_template('add_case.html', officers=officers)
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
            return render_template('edit_case.html', case=case)
        DB_Cases.edit_case(case_id, request.form)
        flash("Case updated successfully!", "info")
        return redirect(url_for('cases.view_cases'))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return render_template('cases.view_cases')
