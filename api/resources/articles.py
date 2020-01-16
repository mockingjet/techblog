from flask import Blueprint, request, abort, jsonify, make_response


api_articles_bp = Blueprint(
    'api_articles',
    __name__,
    url_prefix='/api/articles'
)


mocks = [
    {
        'id': '1',
        'title': 'first post',
        'preview': 'just a few words, don\'t mind',
        'tags': ['Frontend', 'Vue'],
        'content': 'my first post haha',
        'date': '2019/12/30'
    },
    {
        'id': '2',
        'title': 'second post',
        'preview': 'just a few words, don\'t mind',
        'tags': ['Backend', 'Flask'],
        'content': 'my second post haha',
        'date': '2019/12/31'
    },
    {
        'id': '3',
        'title': 'last post',
        'preview': 'just a few words, don\'t mind',
        'tags': ['DevOps', 'Azure'],
        'content': 'my last post haha',
        'date': '2020/01/01'
    },
    {
        'id': '4',
        'title': 'another post',
        'preview': 'just a few words, don\'t mind',
        'tags': ['Flask', 'Nuxt', 'SEO'],
        'content': 'my last post haha',
        'date': '2020/01/01'
    },
    {
        'id': '5',
        'title': 'extra post',
        'tags': ['Axios', 'Http', 'Network'],
        'preview': 'just a few words, don\'t mind',
        'content': 'my last post haha',
        'date': '2020/01/01'
    }
]


@api_articles_bp.route('', methods=['GET', 'POST'])
def articles():
    if request.method == 'GET':
        articles = get_articles()
        rv = {
            "list": articles
        }
        return make_response(jsonify(rv), 200)

    if request.method == 'POST':
        data = request.get_json()
        rv = {
            "id": 1
        }
        return make_response(jsonify(rv), 200)

    abort(400)


@api_articles_bp.route('/<_id>', methods=['GET', 'PUT', 'DELETE'])
def article(_id):
    if request.method == 'GET':
        article = get_article(_id)
        return make_response(jsonify(article), 200)

    abort(400)


def get_articles():
    return mocks


def get_article(_id):
    article = next(filter(lambda obj: obj['id'] == _id, mocks))
    return article
