from ..extension import db
from ..sc_ma import ApplicantSchema
from ..model import Applicant,results
from flask import request, jsonify
from sqlalchemy.sql import func
import json
applicant_schema = ApplicantSchema()
applicants_schema = ApplicantSchema(many=True)


def add_applicant_service():
    data = request.json
    if (data and ('name' in data) and ('email' in data)
            and ('dob' in data) and ('country' in data) and ('status' in data) and ('created_dttm'in data)):
        name = data['name']
        email = data['email']
        dob = data['dob']
        country = data['country']
        status = data['status']
        created_dttm = data['created_dttm']
        try:
            new_applicant = Applicant(name, email, dob, country, status, created_dttm)
            db.session.add(new_applicant)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add applicant!"}), 400
    else:
        return jsonify({"message": "Request error"}), 400


def get_applicant_by_id_service(applicant_id):
    applicant = Applicant.query.get(applicant_id)
    if applicant:
        return applicant_schema.jsonify(applicant)
    else:
        return jsonify({"message": "Not found applicant"}), 404


def get_all_applicant_service():
    applicants = Applicant.query.all()
    if applicants:
        return applicants_schema.jsonify(applicants)
    else:
        return jsonify({"message": "Not found books!"}), 404


def update_applicant_by_service(applicant_id):
    applicant = Applicant.query.get(applicant_id)
    data = request.json
    if applicant:
        if data and "status" in data:
            try:
                applicant.status = data["status"]
                db.session.commit()
                return "applicant Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not delete applicant!"}), 400
    else:
        return "Not found applicant"


def delete_applicant_by_service(applicant_id):
    applicant = Applicant.query.get(applicant_id)
    if applicant:
        try:
            db.session.delete(applicant)
            db.session.commit()
            return "applicant Deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete applicant!"}), 400
    else:
        return "Not found applicant"



