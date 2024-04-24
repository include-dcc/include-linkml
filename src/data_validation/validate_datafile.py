from src.include_linkml.include_pydantic import Study, Participant, Condition, Biospecimen, DataFile
from pydantic import ValidationError


def validate_datafile_entry(row):
    try:
        instance = DataFile(
            # hasStudy=Study(studyCode=row['Study Code'], studyTitle="HTP", program="include"),
            # hasParticipant=Participant(participantExternalId=row['Participant External ID'], familyType="proband_only"),
            # hasBiospecimen=Biospecimen(sampleExternalId=row['Sample External ID'], sampleAvailability="available"),
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
