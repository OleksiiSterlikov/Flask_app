from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required
from app.forms import UploadForm

upload_blueprint = Blueprint('upload', __name__)


@upload_blueprint.route('/upload-csv', methods=['GET', 'POST'])
@login_required
def file_csv():
    form = UploadForm()
    if form.validate_on_submit():
        flash('Everything is OK.', 'success')
        return redirect(url_for('recipient.list'))
    elif form.is_submitted():
        flash('The given data was invalid.', 'danger')
    return render_template('upload/file.html', form=form)
