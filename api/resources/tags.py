from flask_restful import Resource
from models.article import Tag


class TagsResource(Resource):
    def get(self):
        tags = Tag.query.all()
        return {"list": [tag.as_dict for tag in tags]}, 200
