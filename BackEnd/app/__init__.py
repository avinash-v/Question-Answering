from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app,supports_credentials=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

from app import endpoints


