"""Module routes for the object Club"""

from flask import render_template, request, redirect
from app import app, db
from models.models import Club


@app.route('/add-club')
def add_club():
    """Function add Club object"""
    return render_template("add_club.html")

@app.route('/save-club', methods=['POST'])
def save_club():
    """Function save new Club's object"""
    title = request.form.get("title")
    location = request.form.get("location")
    club = Club(title=title, location=location)  
    db.session.add(club)
    db.session.commit()
    return redirect('/')

@app.route("/delete-club/<int:id>")
def delete_club(id):
    """Function delete Club's object at id"""
    club = Club.query.get(id)
    db.session.delete(club)
    db.session.commit()
    return redirect("/")

@app.route("/edit-club/<int:id>")
def edit_club(id):
    """Function edit Club's object at id"""
    club = Club.query.get(id)
    return render_template("add_club.html", club=club)

@app.route("/update-club/<int:id>", methods=["POST"])
def update_club(id):
    """Function update Club's object at id"""
    club = Club.query.get(id)
    club.title = request.form["title"]
    club.location = request.form["location"]
    db.session.add(club)
    db.session.commit()
    return redirect("/")
