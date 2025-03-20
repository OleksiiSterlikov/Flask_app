from app import api, db
from flask_restful import Resource
from flask import request
from models.models import Employee as EmployeeModel


class EmployeesResource(Resource):
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


class SingleEmployeeResource(Resource):
    """Class creating API from single Employee"""
    def get(self, employee_id):
        """Function getting single employee details from API"""
        employee = EmployeeModel.query.get(employee_id)
        return employee.serialize()

    def put(self, employee_id):
        """Function updating single employee details from API"""
        data = request.json
        employee = EmployeeModel.query.get(employee_id)
        employee.first_name = data.get("first_name", employee.first_name)
        employee.last_name = data.get("last_name", employee.last_name)
        employee.email = data.get("email", employee.email)
        employee.club_id = data.get("club_id", employee.club_id)
        db.session.add(employee)
        db.session.commit()
        return employee.serialize()

api.add_resource(EmployeesResource, '/api/v1/employees')
api.add_resource(SingleEmployeeResource, '/api/v1/employees/<employee_id>')
