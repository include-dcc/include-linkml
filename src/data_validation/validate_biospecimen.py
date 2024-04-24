from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen
from pydantic import ValidationError


def validate_biospecimen_entry(row):
    try:
        instance = Biospecimen(
            # hasStudy=Study(studyCode=row['Study Code'], studyTitle="HTP", program="include"),
            # hasParticipant=Participant(participantExternalId=row['Participant External ID'], familyType="proband_only"),
            sampleGlobalId=row['Sample Global ID'],
            sampleExternalId=row['Sample External ID'],
            sampleType=row['Sample Type'],
            ageAtBiospecimenCollection=row['Age At Biospecimen Collection'],
            parentSampleGlobalId=row['Parent Sample Global ID'],
            parentSampleExternalId=row['Parent Sample External ID'],
            parentSampleType=row['Parent Sample Type'],
            collectionGlobalId=row['Collection Global ID'],
            collectionExternalId=row['Collection External ID'],
            collectionSampleType=row['Collection Sample Type'],
            containerGlobalId=row['Container Global ID'],
            containerExternalId=row['Container External ID'],
            volume=row['Volume'],
            volumeUnit=row['Volume Unit'],
            concentration=row['Concentration'],
            concentrationUnit=row['Concentration Unit'],
            laboratoryProcedure=row['Laboratory Procedure'],
            biospecimenStorage=row['Biospecimen Storage'],
            sampleAvailability=row['Sample Availability'],
            containerAvailability=row['Container Availability'],
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Study Code'] + "-" + row['Sample External ID'], e)
        return False, error_details
