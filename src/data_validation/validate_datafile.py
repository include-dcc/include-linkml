from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen, DataFile
from src.data_validation.validation_utils import handle_nan
from pydantic import ValidationError

def validate_datafile_entry(row):
    try:
        instance = DataFile(
            studyCode=row['study code'],
            participantGlobalId=handle_nan(row['participant global id']),
            participantExternalId=handle_nan(row['participant external id']),
            sampleGlobalId=handle_nan(row['sample global id']),
            sampleExternalId=handle_nan(row['sample external id']),
            fileName=handle_nan(row['file name']),
            fileGlobalId=handle_nan(row['file global id']),
            fileS3Location=handle_nan(row['file s3 location']),
            fileUploadLocation=handle_nan(row['file upload location']),
            drsUri=handle_nan(row['drs uri']),
            fileHash=handle_nan(row['file hash']),
            dataAccess=row['data access'],
            dataCategory=row['data category'],
            dataType=handle_nan(row['data type']),
            experimentalStrategy=row['experimental strategy'].split('|') if handle_nan(row['experimental strategy']) else [],
            experimentalPlatform=row['experimental platform'].split('|') if handle_nan(row['experimental platform']) else [],
            fileFormat=handle_nan(row['file format']),
            fileSize=handle_nan(row['file size']),
            fileSizeUnit=handle_nan(row['file size unit'])
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (str(row['sample external id']) + "-" + str(row['file global id']), e)
        return False, error_details
