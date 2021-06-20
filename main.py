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


def abort_if_video_id_doesnt_exist(video_id):
    # abort if video doesnt exist
    if video_id not in videos:
        abort(404, message="Could not find video with that ID")


def abort_if_video_exists(video_id):
    # abort if video already exists
    if video_id in videos:
        abort(409, message="Video already exists with that ID")


class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id)
        # get all the args from video_put_args, if not sent automatically send back error message
        args = video_put_args.parse_args()
        videos[video_id] = args  # add videos
        # 201 is a status code, stands for data created
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204


# Define the Hello World endpoint
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    # Run app in debug mode, see all the output and debug information
    app.run(debug=True)
