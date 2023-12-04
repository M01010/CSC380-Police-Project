from flask import Blueprint, request, render_template, redirect, url_for, flash
from db_officers import DB_Officers
from db_cases import DB_Cases
from db_body_cam import DB_BodyCam
from constants import Constants

officers_blueprint = Blueprint('officers', __name__, template_folder='templates', url_prefix='/officers')


@officers_blueprint.route('/', methods=['GET', 'POST'])
def view_officers():
    try:
        if request.method == 'GET':
            officer_list = DB_Officers.get_officers()
            return render_template('view_officers.html', officers=officer_list)
        officer_list = DB_Officers.get_officers_by_name(request.form['search'])
        return render_template('view_officers.html', officers=officer_list)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return render_template('view_officers.html')


@officers_blueprint.route('/<int:officer_id>')
def view_officer(officer_id):
    try:
        officer = DB_Officers.get_officer(officer_id)
        cases = DB_Cases.get_cases_for_officer(officer_id)
        return render_template('view_officer.html', officer=officer, cases=cases)
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
            body_cams = DB_BodyCam.get_free_body_cams()
            return render_template('add_officer.html', constants=Constants, body_cams=body_cams)
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
            body_cams = DB_BodyCam.get_free_body_cams()
            officer_body_cam = DB_BodyCam.get_body_cam_for_officer(officer_id)
            return render_template('edit_officer.html', officer=officer, constants=Constants,
                                   body_cams=body_cams, officer_body_cam=officer_body_cam)
        DB_Officers.edit_officer(officer_id, request.form)
        flash('Officer updated successfully!', 'info')
        return redirect(url_for('officers.view_officers'))
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('officers.view_officers'))
