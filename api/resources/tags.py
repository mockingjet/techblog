from flask_restful import Resource


class TagsResource(Resource):
    def get(self):
        return {
            "list": [
                {
                    "id": 1,
                    "tag_name": "VueJS"
                }, {
                    "id": 2,
                    "tag_name": "Python"
                }, {
                    "id": 3,
                    "tag_name": "Flask"
                }
            ]
        }, 200
