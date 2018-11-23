from app import api
from flask_restful import Resource,reqparse,fields,marshal
from app.recommendation import Recommendation


api.add_resource(Recommendation,"/recommendation",endpoint="Recommendation")
