from flask import Blueprint, request, render_template, redirect, url_for, flash
from db_body_cam import DB_BodyCam

cases_blueprint = Blueprint('body_cams', __name__, template_folder='templates', url_prefix='/body_cams')


@cases_blueprint.route('/')
def view_body_cams():
    try:
        all_cams = DB_BodyCam.get_body_cams()
        return render_template('view_body_cams.html', all_cams=all_cams)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('home'))


@cases_blueprint.route('/<int:body_cam_id>')
def view_body_cam(body_cam_id):
    try:
        body_cam = DB_BodyCam.get_body_cam(body_cam_id)
        return render_template('view_body_cam.html', body_cam=body_cam)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('body_cams.view_body_cams'))


@cases_blueprint.route('/delete/<int:body_cam_id>')
def delete_body_cam(body_cam_id):
    try:
        DB_BodyCam.delete_body_cam(body_cam_id)
        flash("body cam deleted successfully!", "info")
        return redirect(url_for('body_cams.view_body_cams'))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('body_cams.view_body_cams'))


@cases_blueprint.route('/add', methods=['GET', 'POST'])
def add_body_cam():
    try:
        if request.method == 'GET':
            return render_template('add_body_cam.html')
        DB_BodyCam.add_body_cam(request.form)
        flash("Case added successfully!", "info")
        return redirect(url_for('body_cams.view_body_cam', body_cam_id=request.form['body_cam_id']))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('body_cams.view_body_cams'))


@cases_blueprint.route('/edit/<int:bc_id>', methods=['GET', 'POST'])
def edit_body_cam(bc_id):
    try:
        if request.method == 'GET':
            body_cam = DB_BodyCam.get_body_cam(bc_id)
            return render_template('edit_body_cam.html', body_cam=body_cam)
        DB_BodyCam.edit_body_cam(bc_id, request.form)
        flash("body cam updated successfully!", "info")
        return redirect(url_for('body_cams.view_body_cams'))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('body_cams.view_body_cams'))
