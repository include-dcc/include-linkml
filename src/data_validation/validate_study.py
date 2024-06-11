from src.include_linkml.include_pydantic import Study
from pydantic import ValidationError


def validate_study_entry(row):
    try:
        instance = Study(
            studyCode=row['Study Code'],
            studyTitle=row['Study Title'],
            program=row['Program'].split('|'),
            studyDescription=row['Study Description'],
            principalInvestigatorName=row['Principal Investigator Name'].split('|'),
            studyContactName=row['Study Contact Name'].split('|'),
            studyContactInstitution=row['Study Contact Institution'].split('|'),
            studyContactEmail=row['Study Contact Email'].split('|'),
            vbrEmail=row['VBR Email'],
            vbrUrl=row['VBR URL'],
            vbrReadme=row['VBR Readme'],
            researchDomain=row['Research Domain'].split('|'),
            participantLifespanStage=row['Participant Lifespan Stage'].split('|'),
            selectionCriteria=row['Selection Criteria'],
            studyDesign=row['Study Design'],
            clinicalDataSourceType=row['Clinical Data Source Type'].split('|'),
            dataCategory=row['Data Category'].split('|'),
            studyWebsite=row['Study Website'],
            dbgap=str(row['dbGaP']).split('|'),
            publication=str(row['Publication']).split('|'),
            expectedNumberOfParticipants=int(row['Expected Number of Participants']),
            guidType=row['GUID Type'],
            acknowledgments=row['Acknowledgements'].split('|'),
            citationStatement=row['Citation Statement'].split('|')
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (row['Study Code'], e)
        return False, error_details
