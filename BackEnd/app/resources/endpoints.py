from app import api
from flask_restful import Resource,reqparse,fields,marshal
from app.recommendation import Recommendation
from app.electiveInfo import ElectiveInfo

api.add_resource(Recommendation,"/recommendation",endpoint="Recommendation")
api.add_resource(ElectiveInfo,"/electiveInfo/<courseName>",endpoint="ElectiveInfo")