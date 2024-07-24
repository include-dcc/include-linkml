from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen
from src.data_validation.validation_utils import handle_nan
from pydantic import ValidationError

def validate_biospecimen_entry(row):
    try:
        instance = Biospecimen(
            studyCode=handle_nan(row['study code']),
            participantGlobalId=handle_nan(row['participant global id']),
            participantExternalId=handle_nan(row['participant external id']),
            sampleGlobalId=handle_nan(row['sample global id']),
            sampleExternalId=handle_nan(row['sample external id']),
            sampleType=handle_nan(row['sample type']),
            ageAtBiospecimenCollection=handle_nan(row['age at biospecimen collection']),
            parentSampleGlobalId=handle_nan(row['parent sample global id']),
            parentSampleExternalId=handle_nan(row['parent sample external id']),
            parentSampleType=handle_nan(row['parent sample type']),
            collectionGlobalId=handle_nan(row['collection global id']),
            collectionExternalId=handle_nan(row['collection external id']),
            collectionSampleType=handle_nan(row['collection sample type']),
            containerGlobalId=handle_nan(row['container global id']),
            containerExternalId=handle_nan(row['container external id']),
            volume=handle_nan(row['volume']),
            volumeUnit=handle_nan(row['volume unit']),
            concentration=handle_nan(row['concentration']),
            concentrationUnit=handle_nan(row['concentration unit']),
            laboratoryProcedure=handle_nan(row['laboratory procedure']),
            biospecimenStorage=handle_nan(row['biospecimen storage']),
            sampleAvailability=row['sample availability'],
            containerAvailability=row['container availability']
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (str(row['study code']) + "-" + str(row['sample external id']), e)
        return False, error_details
