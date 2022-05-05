from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import werkzeug
import uuid
import os

from handler import uploadHandler, deleteHandler
from db.actions import Actions

app = Flask(__name__)
api = Api(app)

class Key(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument("id", type=int, location="args")
        args = self.parser.parse_args()

        con = Actions()
        key = con.getKeyDB(args["id"])
        con.closeDB()
        
        return {"key": key}

    def put(self):
        self.parser.add_argument("id", type=int, location="json")
        self.parser.add_argument("key", type=str, location="json")
        args = self.parser.parse_args()

        con = Actions()
        con.editKeyDB(args["id"], args["key"])
        con.closeDB()

        return {"message": "Updated"}

class Domain(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument("id", type=int, location="args")
        args = self.parser.parse_args()

        con = Actions()
        domain = con.getDomainDB(args["id"])
        con.closeDB()
        
        return {"domain": domain}

    def put(self):
        self.parser.add_argument("id", type=int, location="json")
        self.parser.add_argument("domain", type=str, location="json")
        args = self.parser.parse_args()

        con = Actions()
        print(args["id"])
        print(args["domain"])
        con.editDomainDB(args["id"], args["domain"])
        con.closeDB()

        return {"message": "Updated"}

class Upload(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location="files")
        self.parser.add_argument("id", type=str, location="json")
        args = self.parser.parse_args()
        img = args["file"]
        id = int(args["id"])

        filename = uuid.uuid4()
        img.save(f"images/{filename}.png")
   
        con = Actions()

        domain = con.getDomainDB(id)

        uploadInfo = uploadHandler(domain, f"images/tests.png")
        if not "error" in uploadInfo.keys():
            con.addImageDB(uploadInfo["id"], uploadInfo["url"], uploadInfo["del_url"], args["id"], f"{filename}.png")
            con.closeDB()
            return uploadInfo["url"]

        else:
            con.closeDB()
            return uploadInfo

class Delete(Resource):
    def delete(self, id):
        con = Actions()
        delURL = con.getDeleteDB(id)
        pathName = con.getPathDB(id)
        deleteInfo = deleteHandler(delURL)

        if not "error" in deleteInfo.keys():
            con.deleteImageDB(id)
            con.closeDB()
            os.remove(f"images/{pathName}")
            return {"message": "Deleted"}
        else:
            con.closeDB()
            return deleteInfo

class Gallery(Resource):
    def get(self, id):
        con = Actions()
        imageList = con.getAllOwnerDB(id)

        gallery = {}

        for image in imageList:
            gallery[image] = con.getURLDB(image)

        return gallery

class User(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument("id", type=int, location="args")
        args = self.parser.parse_args()

        con = Actions()
        
        domain, key = con.getDomainDB(args["id"]), con.getKeyDB(args["id"])

        con.closeDB()

        return {"domain": domain, "key": key}

    def post(self):
        self.parser.add_argument("id", type=int, location="json")
        args = self.parser.parse_args()

        con = Actions()
        con.addUserDB(args["id"])
        con.closeDB()

        return {"message": "Added"}

    def delete(self):
        self.parser.add_argument("id", type=int, location="json")
        args = self.parser.parse_args()

        con = Actions()
        con.deleteUserDB(args["id"])
        con.closeDB()

        return {"message": "Deleted"}

api.add_resource(Upload, '/upload')
api.add_resource(Delete, '/delete/<id>')
api.add_resource(Key, '/key')
api.add_resource(Domain, '/domain')
api.add_resource(Gallery, '/gallery/<int:id>')
api.add_resource(User, '/user')


if __name__ == '__main__':
    app.run(debug=True)