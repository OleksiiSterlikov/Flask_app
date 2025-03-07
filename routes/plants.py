from app import app
from models.models import Plant
from flask import render_template, request, redirect


@app.route('/add-plant')
def add_plant():
    return render_template("add_plant.html")

@app.route('/save-plant', methods=['POST'])
def save_plant():
    name = request.form.get('name')
    location = request.form.get('location')
    plant = Plant(name, location)
    plant.save()
    return redirect('/')