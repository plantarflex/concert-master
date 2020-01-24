import os
from datetime import datetime, timedelta
from htmlmin.main import minify
import json
from json import JSONDecodeError

from flask import (
    Flask, render_template, jsonify, request, abort,
    send_from_directory, Response, session)
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_migrate import Migrate
from flask_socketio import SocketIO, emit
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token,
    jwt_required, jwt_refresh_token_required, get_jwt_identity,
    get_jti, get_raw_jwt)

from models import *
from serializer import *
from config import Config
from utils import *


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
flask_bcrypt = Bcrypt(app)
jwt = JWTManager(app)
cors = CORS(app)
socketio = SocketIO(app)



@app.route('/')
def home():
    return render_template('index.html')


class LoadPerformList(Resource):
    def post(self):
        data = request.get_json()
        house = data.get('house')
        hall = data.get('hall')
        name = data.get('name')
        start_date = data['startDate']
        end_date = data['endDate']

        performs = Perform.query.\
            filter(Perform.start_date >= start_date).\
            filter(Perform.end_date <= end_date)
        if house is not None:
            performs = performs.filter_by(house=house)
        if hall is not None:
            performs = performs.filter_by(hall=hall)
        if name is not None:
            performs = performs.filter_by(name=name)
        performs = performs.all()
        performs = query_serializer(PerformSchema(), performs)
        return performs


api.add_resource(LoadPerformList, '/api/load/perform_list')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.VIEWER_PORT)
