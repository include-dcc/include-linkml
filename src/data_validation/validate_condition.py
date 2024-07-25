from src.include_linkml.include_pydantic import Study, Participant, Condition
from src.data_validation.validation_utils import handle_nan
from pydantic import ValidationError

def validate_condition_entry(row):
    try:
        instance = Condition(
            studyCode=row['study code'],
            participantGlobalId=handle_nan(row['participant global id']),
            participantExternalId=handle_nan(row['participant external id']),
            eventId=handle_nan(row['event id']),
            eventType=handle_nan(row['event type']),
            conditionMeasureSourceText=handle_nan(row['condition or measure source text']),
            ageAtConditionMeasureObservation=handle_nan(row['age at condition or measure observation']),
            conditionInterpretation=row['condition interpretation'],
            conditionStatus=row['condition status'],
            conditionDataSource=row['condition data source'],
            hpoLabel=handle_nan(row['hpo label']),
            hpoCode=handle_nan(row['hpo code']),
            mondoLabel=handle_nan(row['mondo label']),
            mondoCode=handle_nan(row['mondo code']),
            maxoLabel=handle_nan(row['maxo label']),
            maxoCode=handle_nan(row['maxo code']),
            otherLabel=handle_nan(row['other label']),
            otherCode=handle_nan(row['other code']),
            measureValue=handle_nan(row['measure value']),
            measureUnit=handle_nan(row['measure unit'])
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (str(row['study code']) + "-" + str(row['participant external id']) + "-" + str(row['event id']), e)
        return False, error_details
