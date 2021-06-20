from flask import Flask
from flask_restful import Api, Resource

# Create Flask app
app = Flask(__name__)
# Wrap the app in an API
api = Api(app)

if __name__ == "__main__":
    # Run app in debug mode, see all the output and debug information
    app.run(debug=True)
