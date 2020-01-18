from flask_restful import Resource, reqparse
from flask import request, jsonify
from models.measurement import MeasurementModel
from schemas.measurement import MeasurementSchema

parser = reqparse.RequestParser()

measurement_schema = MeasurementSchema()


class Measurement(Resource):
    @classmethod
    def post(cls):
        measurement_json = request.get_json()
        measurement = measurement_schema.load(measurement_json)
        measurement.save_to_db()
        return 201


