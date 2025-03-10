"""Modul routes for the object Employee"""

from flask import render_template
from app import app, db
from models.models import Employee


@app.route('/employees')
def employees_home():
    """Function to display employees home page."""
    employees = Employee.query.all()
    return render_template("employee-list.html", employees=employees)
