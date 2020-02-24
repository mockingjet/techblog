from datetime import datetime
from models.base import db, Base


article_to_tag = db.Table(
    'articles_to_tags',
    db.Column(
        'article_id', db.Integer, db.ForeignKey('articles.article_id'), primary_key=True),
    db.Column(
        'tag_id', db.Integer, db.ForeignKey('tags.tag_id'), primary_key=True)
)


class Article(Base):
    __tablename__ = "articles"

    article_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    preview = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.relationship(
        "Tag", secondary=article_to_tag, back_populates="articles")
    created_at = db.Column(
        db.Text,
        default=datetime.utcnow,
        nullable=False
    )

    def __init__(self, tags, title, preview, content):
        self.tags = tags
        self.title = title
        self.preview = preview
        self.content = content

    @property
    def view(self):
        _dict = self.as_dict()
        _dict.update({
            "tags": [tag.as_dict()['tag_name'] for tag in self.tags]
        })
        return _dict


class Tag(Base):
    __tablename__ = "tags"
    tag_id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(30), nullable=False, unique=True)
    articles = db.relationship(
        "Article", secondary=article_to_tag, back_populates="tags")

    def __init__(self, tag_name):
        self.tag_name = tag_name
