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
            expectedNumberOfParticipants=int(row['Expected Number of Participants']),
            expectedNumberOfFiles=int(row['Expected Number of Files']),
            dataCollectionStartYear=row['Data Collection Start Year'],
            dataCollectionEndYear=row['Data Collection End Year'],
            dataCategory=row['Data Category'],
            dataType=row['Data Type'],
            experimentalStrategy=str(row['Experimental Strategy']).split('|'),
            experimentalPlatform=str(row['Experimental Platform']).split('|'),
            publication=str(row['Publication']).split('|'),
            accessLimitations=row['Access Limitations'],
            accessRequirements=row['Access Requirements'],
            dbgap=str(row['DbGaP']).split('|'),
            otherRepository=row['Other Repository'],
            otherAccessAuthority=row['Other Access Authority'],
            isHarmonized=bool(row['Is Harmonized?'])
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Dataset Name'] + "-" + str(row['Dataset External ID']), e)
        return False, error_details
