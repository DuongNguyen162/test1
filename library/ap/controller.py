from flask import Blueprint
from .services import (add_applicant_service, get_applicant_by_id_service,
                       get_all_applicant_service,update_applicant_by_service, delete_applicant_by_service)
applicant = Blueprint("applicant", __name__)

# add a new client


@applicant.route("/applicant", methods=['POST'])
def add_applicant():
    return add_applicant_service()

# get applicant by id


@applicant.route("applicant/<int:applicant_id>", methods=['GET'])
def get_applicant_by_id(applicant_id):
    return get_applicant_by_id_service(applicant_id)

# get all applicant


@applicant.route("/applicant", methods=['GET'])
def get_all_applicant():
    return get_all_applicant_service()

# update applicant


@applicant.route("/applicant/<int:applicant_id>", methods=['PUT'])
def update_applicant_by_service(applicant_id):
    return update_applicant_by_service(applicant_id)

# delete applicant


@applicant.route("/book-management/book/<int:id>", methods=['DELETE'])
def delete_applicant_by_service(applicant_id):
    return delete_applicant_by_service(applicant_id)



