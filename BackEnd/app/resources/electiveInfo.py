from flask_restful import Resource,reqparse,fields,marshal
from flask import request
from app.models import User,Elective
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity
from flask import jsonify
from datetime import datetime
from app import db
from flask_cors import CORS,cross_origin
import json

headers = {"Content-Type": "application/json"}


class ElectiveInfo(Resource):
	@cross_origin(origins="*",supports_credentials=True)
	def get(self,courseName):
		e = Elective.query.filter_by(courseName=courseName).first()
		if e is None:
			return jsonify({"description":"No such course exists"}),headers,200
		res = {"courseName":e.courseName,"description":e.description,"teacher":e.teacher,"specialization":e.specialization,"prerequisites":e.prerequisites}
		return jsonify(res),headers,200






