"""Module routes for the object Club"""

from flask import render_template, request, redirect
from app import app



@app.route('/add-club')
def add_club():
    """Function add Club object"""
    return render_template("add_club.html")

@app.route('/save-club', methods=['POST'])
def save_club():
    """Function save new Club object"""
    
    return redirect('/')

@app.route("/delete-club/<int:id>")
def delete_club(id):
    """Function delete Club object at id"""
    
    return redirect("/")
