from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen, DataFile
from pydantic import ValidationError


def validate_datafile_entry(row):
    try:
        instance = DataFile(
            studyCode=row['Study Code'],
            participantGlobalId=row['Participant Global ID'],
            participantExternalId=row['Participant External ID'],
            sampleGlobalId=row['Sample Global ID'],
            sampleExternalId=row['Sample External ID'],
            fileGlobalId=row['File Global ID'],
            fileExternalId=row['File External ID'],
            fileName=row['File Name'],
            fileHash=row['File Hash'],
            dataAccess=row['Data Access'],
            dataCategory=row['Data Category'],
            dataType=row['Data Type'],
            experimentalStrategy=row['Experimental Strategy'],
            experimentalPlatform=row['Experimental Platform'],
            fileFormat=row['File Format'],
            fileSize=row['File Size'],
            fileSizeUnit=row['File Size Unit'],
            accessUrl=row['Access URL'],
            publicationDoi=row['Publication DOI']
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Sample External ID'] + "-" + row['File External ID'], e)
        return False, error_details
