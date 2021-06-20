from flask import Flask
from flask_restful import Api, Resource

# Create Flask app
app = Flask(__name__)
# Wrap the app in an API
api = Api(app)

videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        return


# Define the Hello World endpoint
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    # Run app in debug mode, see all the output and debug information
    app.run(debug=True)
