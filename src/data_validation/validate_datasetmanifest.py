from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen, DataFile, Dataset, DatasetManifest
from pydantic import ValidationError


def validate_datasetmanifest_entry(row):
    try:
        instance = DatasetManifest(
            studyCode=row['Study Code'],
            datasetName=row['Dataset Name'],
            datasetGlobalId=row['Dataset Global ID'],
            datasetExternalId=row['Dataset External ID'],
            fileName=row['File Name'],
            fileGlobalId=row['File Global ID']
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Dataset Name'] + "-" + str(row['Dataset External ID']), e)
        return False, error_details
