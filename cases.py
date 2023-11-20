from flask import Blueprint, request, render_template, redirect, url_for, flash
from database import Database

cases = Blueprint('cases', __name__, template_folder='templates', url_prefix='/cases')

# Route to view all cases
@cases.route('/')
def view_cases():
    try:
        all_cases = Database.Cases.get_cases()
        return render_template('view_cases.html', cases=all_cases)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('home'))

# Route to view a single case
@cases.route('/<int:case_id>')
def view_case(case_id):
    try:
        case = Database.Cases.get_case(case_id)
        if case:
            return render_template('view_case.html', case=case)
        else:
            flash("Case not found.", "warning")
            return redirect(url_for('cases.view_cases'))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('cases.view_cases'))

# Route to add a new case
@cases.route('/add', methods=['GET', 'POST'])
def add_case():
    officers = Database.Officers.get_officers()  # Fetch the officers for the dropdown
    if request.method == 'POST':
        try:
            # Assuming 'case_id' is provided by the form and you want to manually insert it.
            case_id = request.form.get('case_id')

            # Validate that the case_id is numeric and does not already exist in the database
            if not case_id.isdigit():
                flash('Invalid Case ID. Please enter a numeric value.', 'danger')
                return render_template('add_case.html', officers=officers, case=request.form)

            existing_case = Database.Cases.get_case(case_id)
            if existing_case:
                flash('Case ID already exists. Please enter a unique Case ID.', 'danger')
                return render_template('add_case.html', officers=officers, case=request.form)

            # Proceed with adding the case to the database
            case_data = {
                'case_id': case_id,  # Include the case_id in the case_data dictionary
                'case_type': request.form['case_type'],
                'status': request.form['status'],
                'date_reported': request.form['date_reported'],
                'officer_id': request.form['officer_id']
            }
            Database.Cases.add_case(case_data)
            flash("Case added successfully!", "info")
            # Redirect to the view case page for the newly created case
            return redirect(url_for('cases.view_case', case_id=case_id))
        except Exception as e:
            flash(f"Error: {e}", "danger")

    # For a GET request, just show the empty form
    return render_template('add_case.html', officers=officers)


# Route to edit a case
@cases.route('/edit/<int:case_id>', methods=['GET', 'POST'])
def edit_case(case_id):
    if request.method == 'POST':
        try:
            case_data = {
                'case_type': request.form['case_type'],
                'status': request.form['status'],
                'date_reported': request.form['date_reported'],
                'officer_id': request.form['officer_id']
            }
            Database.Cases.edit_case(case_id, case_data)
            flash("Case updated successfully!", "info")
            return redirect(url_for('cases.view_cases'))
        except Exception as e:
            flash(f"Error: {e}", "danger")

    case = Database.Cases.get_case(case_id)
    if not case:
        flash("Case not found.", "warning")
        return redirect(url_for('cases.view_cases'))

    return render_template('edit_case.html', case=case)

# Route to delete a case
@cases.route('/delete/<int:case_id>')
def delete_case(case_id):
    try:
        Database.Cases.delete_case(case_id)
        flash("Case deleted successfully!", "info")
    except Exception as e:
        flash(f"Error: {e}", "danger")
    return redirect(url_for('cases.view_cases'))
