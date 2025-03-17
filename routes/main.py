"""Modul main routes"""

from flask import render_template, request, session, redirect
from app import app, db
from models.models import Club, User


@app.route('/')
def main():
    """Main function"""
    clubs = Club.query.order_by(Club.title.asc()).all()
    user = None
    if session.get('user', False):
        user = User.query.get(session.get('user'))
    return render_template('index.html', clubs=clubs, user=user)


@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    """Sign in function"""
    if request.method == 'POST':
        data = request.form
        user = User(
            username=data.get('username'), 
            first_name=data.get('first_name'), 
            last_name=data.get('last_name'),
            email=data.get('email'),
            password=data.get('password')
            )
        db.session.add(user)
        db.session.commit()
        session['user'] = user.id
        return redirect('/')
    else:
        return render_template('sign-up.html')
