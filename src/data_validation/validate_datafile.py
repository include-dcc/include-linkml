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
            fileName=row['File Name'],
            fileGlobalId=row['File Global ID'],
            fileS3Location=row['File S3 Location'],
            fileUploadLocation=row['File Upload Location'],
            drsUri=row['DRS URI'],
            fileHash=row['File Hash'],
            dataAccess=row['Data Access'],
            dataCategory=row['Data Category'],
            dataType=row['Data Type'],
            experimentalStrategy=str(row['Experimental Strategy']).split('|'),
            experimentalPlatform=str(row['Experimental Platform']).split('|'),
            fileFormat=row['File Format'],
            fileSize=int(row['File Size']),
            fileSizeUnit=row['File Size Unit']
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Sample External ID'] + "-" + row['File Global ID'], e)
        return False, error_details
