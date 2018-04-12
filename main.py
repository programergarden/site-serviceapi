from flask import Flask, jsonify
from config import DevelopConfig
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config.from_object(DevelopConfig)

@app.route('/')
def index():
    return '<h1>Welcome Programergarden API</h1><p>this is Programergarden.net api site,by python 3.4 flask</p>'

if __name__ == '__main__':
    # Entry the application
    app.run()