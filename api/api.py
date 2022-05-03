from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import werkzeug
import uuid

from handler import upload


app = Flask(__name__)
api = Api(app)

class Upload(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location="files")
        args = self.parser.parse_args()
        img = args["file"]
        filename = uuid.uuid4()
        img.save(f"images/{filename}.png")

        upload("https://please-fuck.me/", f"images/{filename}.png")
        




api.add_resource(Upload, '/upload')


if __name__ == '__main__':
    app.run(debug=True)