from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen, DataFile, Dataset
from pydantic import ValidationError


def validate_dataset_entry(row):
    try:
        instance = Dataset(
            studyCode=row['Study Code'],
            datasetName=row['Dataset Name'],
            datasetDescription=row['Dataset Description'],
            datasetGlobalId=row['Dataset Global ID'],
            datasetExternalId=row['Dataset External ID'],
            datasetExpectedNumberOfParticipants=row['Dataset Expected Number of Participants'],
            expectedNumberOfFiles=row['Expected Number of Files'],
            dataCollectionStartYear=row['Data Collection Start Year'],
            dataCollectionEndYear=row['Data Collection End Year'],
            datasetDataCategory=row['Dataset Data Category'],
            datasetDataType=row['Dataset Data Type'],
            datasetExperimentalStrategy=row['Dataset Experimental Strategy'],
            datasetExperimentalPlatform=row['Dataset Experimental Platform'],
            datasetPublication=str(row['Dataset Publication']).split('|'),
            accessLimitations=row['Access Limitations'],
            accessRequirements=row['Access Requirements'],
            datasetDbgap=str(row['Dataset DbGaP']).split('|'),
            otherRepository=row['Other Repository'],
            otherAccessAuthority=row['Other Access Authority']
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Dataset Name'] + "-" + str(row['Dataset External ID']), e)
        return False, error_details
