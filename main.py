from flask import Flask
from flask_restful import Api, Resource

# Create Flask app
app = Flask(__name__)
# Wrap the app in an API
api = Api(app)


class HelloWorld(Resource):
    # Override the GET method
    def get(self, name, test):
        return {"name": name, "test": test}

    def post(self):
        return {"data": "posted"}


# Define the Hello World endpoint
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

if __name__ == "__main__":
    # Run app in debug mode, see all the output and debug information
    app.run(debug=True)
