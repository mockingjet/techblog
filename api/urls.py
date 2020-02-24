from flask_restful import Api
from resources.articles import ArticlesResource, ArticleResource
from resources.tags import TagsResource

api = Api()

api.add_resource(ArticlesResource, "/api/articles")
api.add_resource(ArticleResource, "/api/articles/<article_id>")
api.add_resource(TagsResource, "/api/tags")
