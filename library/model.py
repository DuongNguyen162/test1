from datetime import datetime
import random
from extension import db
import enum
from sqlalchemy.sql import func
import secrets
class Country(enum.Enum):
    Vietnam = "704"
    American = "113"
    Ukraine = "114"
    UnitedArabEmirates ="119" 
    NorthernIreland = "110"
    UnitedStatesofAmerica ="115" 
    UnitedStatesMinorOutlyingIslands ="116" 
    Uruguay = "117"
    Uzbekistan = "118"
    India = "356"
    Indonesia = "225"
    Iran = "324"
    Iraq = "412"
    Ireland = "761"



class Applicant(db.Model):
    applicant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    dob = db.Column(db.Date)
    country = db.Column(db.Enum(Country))
    status = db.Column(db.String(100), default = "pending" )
    created_dttm = db.Column(db.DateTime, default=datetime.utcnow())
    


    def __init__(self, name, email, dob, country,status,created_dttm): 
        self.name = name
        self.email = email
        self.dob = dob
        self.country = country
        self.status = status 
        self.created_dttm = created_dttm

class results():
    applicant_id = db.Column(db.Integer, db.ForeignKey('Applicant.applicant_id'))
    client_key = db.Column(db.String(128)) 
    applicant_status = db.Column(db.String(100))
    processed_dttm = db.Column(db.DateTime, default=datetime.utcnow())
    
    def key_client(self,client_key):
        self.client_key = client_key(random(secrets.token_hex(16)))
    

    def __init__(self,applicant_status,processed_dttm):
        self.applicant_status = applicant_status
        self.processed_dttm = processed_dttm