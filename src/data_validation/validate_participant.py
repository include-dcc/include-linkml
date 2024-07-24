from src.include_linkml.include_pydantic import Study, Participant
from src.data_validation.validation_utils import handle_nan
from pydantic import ValidationError

def validate_participant_entry(row):
    try:
        instance = Participant(
            studyCode=row['study code'],
            participantGlobalId=handle_nan(row['participant global id']),
            participantExternalId=handle_nan(row['participant external id']),
            familyId=handle_nan(row['family id']),
            familyType=row['family type'],
            fatherId=handle_nan(row['father id']),
            motherId=handle_nan(row['mother id']),
            siblingId=handle_nan(row['sibling id']),
            otherFamilyMemberId=handle_nan(row['other family member id']),
            familyRelationship=row['family relationship'],
            sex=row['sex'],
            race=row['race'],
            ethnicity=row['ethnicity'],
            downSyndromeStatus=row['down syndrome status'],
            ageAtFirstPatientEngagement=handle_nan(row['age at first patient engagement']),
            firstPatientEngagementEvent=handle_nan(row['first patient engagement event']),
            outcomesVitalStatus=row['outcomes vital status'],
            ageAtLastVitalStatus=handle_nan(row['age at last vital status'])
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (str(row['study code']) + "-" + str(row['participant external id']), e)
        return False, error_details
