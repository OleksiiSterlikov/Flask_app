from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required

from app.forms import LoginForm, RegistrationForm
from app.models import User

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.authenticate(form.user_id.data, form.password.data)
        if user:
            login_user(user)
            flash('Login successful.', 'success')
            return redirect(url_for('main.index'))
        flash('Login unsuccessful.', 'danger')
    return render_template('auth/login.html', form=form)

@auth_blueprint.route('/logout')
def logout():
    logout_user()
    flash('Logout successful.', 'success')
    return redirect(url_for('main.index'))

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.data)
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        user.save()
        login_user(user)
        flash('Registration successful.', 'success')
        return redirect(url_for('main.index'))
    elif form.is_submitted():
        flash('Registration failed.', 'danger')
    return render_template('auth/register.html', form=form)
