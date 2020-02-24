from flask import request
from flask_restful import Resource
from models.article import Article, Tag


class ArticlesResource(Resource):
    def get(self):
        articles = Article.query.all()
        article_list = [article.view for article in articles]
        return {"list": article_list}, 200

    def post(self):
        req = request.json

        # 處理新的tags
        _tags = req.pop("tags")
        tags = []
        for _tag in _tags:
            tag = Tag.query.filter_by(tag_name=_tag['tag_name']).first()
            if not tag:
                new = Tag(_tag['tag_name']).save()
                tags.append(new)
            else:
                tags.append(tag)

        article = Article(
            tags=tags,
            title=req.pop('title'),
            preview=req.pop('preview'),
            content=req.pop('content'),
        )

        article.save()

        return {'id': article.article_id}, 200


class ArticleResource(Resource):
    def get(self, article_id):
        return {
            "id": article_id,
            "tags": "1,2,3,4",
                    "title": "測試",
                    "preview": "預覽",
                    "content": "內容",
                    "created_at": "2020/01/20 20:40:17"
        }, 200
