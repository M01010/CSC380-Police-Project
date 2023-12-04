from flask import Blueprint, request, render_template, redirect, url_for, flash
from db_videos import DB_Videos
from db_body_cam import DB_BodyCam

cases_blueprint = Blueprint('videos', __name__, template_folder='templates', url_prefix='/videos')


@cases_blueprint.route('/')
def view_videos():
    try:
        all_videos = DB_Videos.get_videos()
        return render_template('view_videos.html', all_videos=all_videos)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('home'))


@cases_blueprint.route('/<int:video_id>')
def view_video(video_id):
    try:
        video = DB_Videos.get_video(video_id)
        return render_template('view_video.html', video=video)
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('videos.view_videos'))


@cases_blueprint.route('/delete/<int:video_id>')
def delete_video(video_id):
    try:
        DB_Videos.delete_video(video_id)
        flash("video deleted successfully!", "info")
        return redirect(url_for('videos.view_videos'))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('videos.view_videos'))


@cases_blueprint.route('/add', methods=['GET', 'POST'])
def add_video():
    try:
        if request.method == 'GET':
            return render_template('add_video.html')
        DB_Videos.add_video(request.form)
        flash("video added successfully!", "info")
        return redirect(url_for('videos.view_video', video_id=request.form['video_id']))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('videos.view_videos'))


@cases_blueprint.route('/edit/<int:video_id>', methods=['GET', 'POST'])
def edit_video(video_id):
    try:
        if request.method == 'GET':
            video = DB_Videos.get_video(video_id)
            body_cam = DB_BodyCam.get_body_cam(video['BODY_CAM_body_cam_id'])
            body_cams = DB_BodyCam.get_body_cams()
            return render_template('edit_body_cam.html', video=video, body_cam=body_cam, body_cams=body_cams)
        DB_Videos.edit_video(video_id, request.form)
        flash("video updated successfully!", "info")
        return redirect(url_for('videos.view_videos'))
    except Exception as e:
        flash(f"Error: {e}", "danger")
        return redirect(url_for('videos.view_videos'))
