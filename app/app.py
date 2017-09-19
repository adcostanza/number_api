from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from json import dumps
from db import DB

numbers = DB()

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser() #parse POST requests
parser.add_argument('number') #phone number
parser.add_argument('token') #JWT token
class Numbers(Resource):
	def get(self):
		return numbers.selectNumbers()
	def post(self):
		args = parser.parse_args() #POST requests
		get_args = request.args #GET variables
		token = get_args['token'] #jwt token
		numbers.addNumber(args['number'])
		return (get_args,201)

api.add_resource(Numbers,'/numbers')
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080)
    