from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen, DataFile, Dataset
from src.data_validation.validation_utils import handle_nan
from pydantic import ValidationError

def validate_dataset_entry(row):
    try:
        instance = Dataset(
            studyCode=row['study code'],
            datasetName=handle_nan(row['dataset name']),
            datasetDescription=handle_nan(row['dataset description']),
            datasetGlobalId=handle_nan(row['dataset global id']),
            datasetExternalId=handle_nan(row['dataset external id']),
            expectedNumberOfParticipants=handle_nan(row['expected number of participants']),
            expectedNumberOfFiles=handle_nan(row['expected number of files']),
            dataCollectionStartYear=handle_nan(row['data collection start year']),
            dataCollectionEndYear=handle_nan(row['data collection end year']),
            dataCategory=row['data category'],
            dataType=handle_nan(row['data type']),
            experimentalStrategy=row['experimental strategy'].split('|') if handle_nan(row['experimental strategy']) else [],
            experimentalPlatform=row['experimental platform'].split('|') if handle_nan(row['experimental platform']) else [],
            publication=row['publication'].split('|') if handle_nan(row['publication']) else [],
            accessLimitations=handle_nan(row['access limitations']),
            accessRequirements=handle_nan(row['access requirements']),
            dbgap=row['dbgap'].split('|') if handle_nan(row['dbgap']) else [],
            otherRepository=handle_nan(row['other repository']),
            otherAccessAuthority=handle_nan(row['other access authority']),
            isHarmonized=bool(row['is harmonized?'])
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['dataset name'] + "-" + str(row['dataset external id']), e)
        return False, error_details
