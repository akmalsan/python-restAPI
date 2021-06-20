from flask import Flask
from flask_restful import Api, Resource

# Create Flask app
app = Flask(__name__)
# Wrap the app in an API
api = Api(app)

names = {"tom": {"age": 19, "gender": "male"},
         "dee": {"age": 19, "gender": "female"}}


class HelloWorld(Resource):
    # Override the GET method
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "posted"}


# Define the Hello World endpoint
api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    # Run app in debug mode, see all the output and debug information
    app.run(debug=True)
