from flask import Blueprint, request, abort, jsonify, make_response


api_tags_bp = Blueprint(
    'api_tags',
    __name__,
    url_prefix='/api/tags'
)

mocks = [
    "Frontend",
    "Backend",
    "DevOps",
    "Design Pattern",
    "Algorithmn",
    "PWA",
    "Nuxt",
    "Vue",
    "Flask",
    "Azure",
    "Frontend",
    "Backend",
    "DevOps",
    "Design Pattern",
    "Algorithmn",
    "PWA",
    "Nuxt",
    "Vue",
    "Flask",
    "Azure"
]


@api_tags_bp.route('', methods=['GET', 'POST'])
def tags():
    if request.method == 'GET':
        tags = get_tags()
        return make_response(jsonify(tags), 200)

    if request.method == 'POST':
        print(request.args)
        return make_response(jsonify(), 200)

    abort(400)


def get_tags():
    return mocks
