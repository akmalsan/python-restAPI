from flask import Flask
from flask_restful import Api, Resource, reqparse

# Create Flask app
app = Flask(__name__)
# Wrap the app in an API
api = Api(app)

# create request parser object to parse through requests, make sure it follows the args guidelines
video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument(
    "views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument(
    "likes", type=int, help="Likes of the video is required", required=True)

videos = {}

# abort if video doesnt exist


def abort_if_video_id_null(video_id):
    if video_id not in videos:
        abort("Video id is not valid")


class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_null(video_id)
        return videos[video_id]

    def put(self, video_id):
        # get all the args from video_put_args, if not sent automatically send back error message
        args = video_put_args.parse_args()
        videos[video_id] = args  # add videos
        # 201 is a status code, stands for data created
        return videos[video_id], 201


# Define the Hello World endpoint
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    # Run app in debug mode, see all the output and debug information
    app.run(debug=True)
