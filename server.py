#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///ctlihr.db')
app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    
class TotalLeaves(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select leaves_total from employees where id =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    
class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select name from employees where id =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class AppliedLeaves(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select leaves_applied from employees where id =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class BalanceLeaves(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select leaves_balance from employees where id =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_2
api.add_resource(TotalLeaves, '/totalLeaves/<employee_id>') # Route_3
api.add_resource(AppliedLeaves, '/appliedLeaves/<employee_id>') # Route_4
api.add_resource(BalanceLeaves, '/balanceLeaves/<employee_id>') # Route_5


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5051)
