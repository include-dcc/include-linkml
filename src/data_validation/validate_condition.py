from src.include_linkml.include_pydantic import Study, Participant, Condition
from pydantic import ValidationError


def validate_condition_entry(row):
    try:
        instance = Condition(
            # hasStudy=Study(studyCode=row['Study Code'], studyTitle="HTP", program="include"),
            # hasParticipant=Participant(participantExternalId=row['Participant External ID'], familyType="proband_only"),
            eventId=row['Event ID'],
            eventType=row['Event Type'],
            conditionMeasureSourceText=row['Condition or Measure Source Text'],
            ageAtConditionMeasureObservation=row['Age At Condition or Measure Observation'],
            conditionInterpretation=row['Condition Interpretation'],
            conditionStatus=row['Condition Status'],
            conditionDataSource=row['Condition Data Source'],
            hpoLabel=row['HPO Label'],
            hpoCode=row['HPO Code'],
            mondoLabel=row['MONDO Label'],
            mondoCode=row['MONDO Code'],
            maxoLabel=row['MAXO Label'],
            maxoCode=row['MAXO Code'],
            otherLabel=row['Other Label'],
            otherCode=row['Other Code'],
            measureValue=row['Measure Value'],
            measureUnit=row['Measure Unit']
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Study Code'] + "-" + str(row['Participant External ID']) + "-" + row['Event ID'], e)
        return False, error_details
