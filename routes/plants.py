"""Module routes for the object Plant"""

from flask import render_template, request, redirect
from app import app
from models.models import Plant


@app.route('/add-plant')
def add_plant():
    """Function add Plant object"""
    return render_template("add_plant.html")

@app.route('/save-plant', methods=['POST'])
def save_plant():
    """Function save new Plant object"""
    name = request.form.get('name')
    location = request.form.get('location')
    plant = Plant(name, location)
    plant.save()
    return redirect('/')

@app.route("/delete-plant/<int:id>")
def delete_plant(id):
    """Function delete Plant object at id"""
    Plant.delete(id)
    return redirect("/")
