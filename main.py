from flask import Flask
from flask_restful import Api, Resource

# Create Flask app
app = Flask(__name__)
# Wrap the app in an API
api = Api(app)

# Create a class that is a Resource, override several methods from Resource


class HelloWorld(Resource):
    # Override the GET method
    def get(self):
        return {"Hello World"}


# Define the Hello World endpoint
api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    # Run app in debug mode, see all the output and debug information
    app.run(debug=True)
