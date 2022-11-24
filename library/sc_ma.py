from extension import ma


class ApplicantSchema(ma.Schema):
    class Meta:
        fields = ('applicant_id', 'name', 'email', 'dob', 'country','status','created_dttm')


class App_outSchema(ma.Schema):
    class Meta:
        fields = ('applicant_id', 'status')


class ProcessResultsSchema(ma.Schema):
    class Meta:
        fields = ('applicant_id', 'client_key','applicant_status','processed_dttm')



