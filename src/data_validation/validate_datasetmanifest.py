from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen, DataFile, Dataset, DatasetManifest
from src.data_validation.validation_utils import handle_nan
from pydantic import ValidationError

def validate_datasetmanifest_entry(row):
    try:
        instance = DatasetManifest(
            studyCode=row['study code'],
            datasetName=handle_nan(row['dataset name']),
            datasetGlobalId=handle_nan(row['dataset global id']),
            datasetExternalId=handle_nan(row['dataset external id']),
            fileName=handle_nan(row['file name']),
            fileGlobalId=handle_nan(row['file global id'])
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (str(row['dataset name']) + "-" + str(row['dataset external id']), e)
        return False, error_details
