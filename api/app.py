from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from resources.articles import api_articles_bp

#####################################################
app = Flask(__name__)
client = 'http://192.168.1.113:3000'
CORS(app, resources={r"/api/*": {"origins": client}})
#####################################################


@app.route('/')
def hello():
    return 'Hello, World!'


app.register_blueprint(api_articles_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
