from src.include_linkml.include_pydantic import Study, Participant
from pydantic import ValidationError


def validate_participant_entry(row):
    try:
        instance = Participant(
            # hasStudy=Study(studyCode=row['Study Code'], studyTitle="HTP", program="include"),
            participantGlobalId=row['Participant Global ID'],
            participantExternalId=row['Participant External ID'],
            familyId=row['Family ID'],
            familyType=row['Family Type'],
            fatherId=row['Father ID'],
            motherId=row['Mother ID'],
            siblingId=row['Sibling ID'],
            otherFamilyMemberId=row['Other Family Member ID'],
            familyRelationship=row['Family Relationship'],
            sex=row['Sex'],
            race=row['Race'],
            ethnicity=row['Ethnicity'],
            downSyndromeStatus=row['Down Syndrome Status'],
            ageAtFirstPatientEngagement=row['Age at First Patient Engagement'],
            firstPatientEngagementEvent=row['First Patient Engagement Event'],
            outcomesVitalStatus=row['Outcomes Vital Status'],
            ageAtLastVitalStatus=row['Age at Last Vital Status']
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Study Code'] + "-" + row['Participant External ID'], e)
        return False, error_details
