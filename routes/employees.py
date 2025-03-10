"""Modul routes for the object Employee"""

from flask import render_template, request, redirect
from app import app, db
from models.models import Employee, Club


@app.route('/employees')
def employees_home():
    """Function to display employees home page."""
    employees = Employee.query.all()
    return render_template("employee-list.html", employees=employees)

@app.route('/add-employee', methods=['POST', 'GET'])
def add_employee():
    """Function to add employee"""
    if request.method == "POST":
        data = request.form
        try:
            employee = Employee(
                first_name=data.get("first_name"), 
                last_name=data.get("last_name"), 
                email=data.get("email"),
                club_id=int(data.get("club_id"))
                )
            db.session.add(employee)
            db.session.commit()
        except:
            return "This email already exist!"
        return redirect("/employees")
    else:
        clubs = Club.query.all()
        return render_template('add-employee.html', clubs=clubs)
