from app import api
from flask_restful import Resource
from models.models import Employee as EmployeeModel


class Employees(Resource):
    """Class creating API from Employee"""
    def get(self):
        """Function getting employee details from API"""
        employees = EmployeeModel.query.all()
        employee_data = []
        for employee in employees:
            employee_data.append(employee.serialize())
        return employee_data


api.add_resource(Employees, '/api/v1/employees')
