from ast import parse
from unittest import result
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class calculator(Resource):

    def get(self):

        parser = reqparse.RequestParser()

        parser.add_argument('num_1', type=float)
        parser.add_argument('num_2', type=float)
        parser.add_argument('operation', type=str)

        a = parser.parse_args().get('num_1')
        b = parser.parse_args().get('num_2')
        operation = parser.parse_args().get('operation')

        if operation == 'add':
            result = a + b

        elif operation == 'subtract':
            result = a - b

        elif operation == 'multiply':
            result = a * b

        elif operation == 'divide':
            result = a / b

        else:
            result = "Not a supported operation!"

        return jsonify(result=result)

api.add_resource(calculator, '/calculate')

if __name__ == '__main__':
    app.run(debug=True)