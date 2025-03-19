from app import api, db
from flask_restful import Resource
from flask import request
from models.models import Employee as EmployeeModel


class Employees(Resource):
    """Class creating API from Employee"""
    def get(self):
        """Function getting employee details from API"""
        filter = request.args
        query = EmployeeModel.query
        if len(filter) < 1:
            employees = query.all()
        else:
            for key in filter.keys():
                employees = query.filter(getattr(EmployeeModel, key) == filter.get(key))

        employee_data = []
        for employee in employees:
            employee_data.append(employee.serialize())
        return employee_data

    def post(self):
        """Function creating employee from API"""
        data = request.json
        employee = EmployeeModel(
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            club_id=int(data.get("club_id"))
        )
        db.session.add(employee)
        db.session.commit()
        return employee.serialize()


api.add_resource(Employees, '/api/v1/employees')
