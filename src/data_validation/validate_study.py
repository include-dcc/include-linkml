from src.include_linkml.include_pydantic import Study
from src.data_validation.validation_utils import handle_nan
from pydantic import ValidationError


def validate_study_entry(row):
    try:
        instance = Study(
            studyCode = row['study code'],
            studyTitle = handle_nan(row['study title']),
            program = row['program'].split('|'),
            studyDescription = handle_nan(row['study description']),
            principalInvestigatorName = handle_nan(row['principal investigator name']).split('|') if handle_nan(row['principal investigator name']) else [],
            studyContactName = handle_nan(row['study contact name']).split('|') if handle_nan(row['study contact name']) else [],
            studyContactInstitution = handle_nan(row['study contact institution']).split('|') if handle_nan(row['study contact institution']) else [],
            studyContactEmail = handle_nan(row['study contact email']).split('|') if handle_nan(row['study contact email']) else [],
            vbrEmail = handle_nan(row['vbr email']),
            vbrUrl = handle_nan(row['vbr url']),
            vbrReadme = handle_nan(row['vbr readme']),
            researchDomain = row['research domain'].split('|'),
            participantLifespanStage = row['participant lifespan stage'].split('|'),
            selectionCriteria = handle_nan(row['selection criteria']),
            studyDesign = handle_nan(row['study design']),
            clinicalDataSourceType = row['clinical data source type'].split('|'),
            dataCategory = row['data category'].split('|'),
            studyWebsite = handle_nan(row['study website']),
            dbgap = row['dbgap'].split('|') if handle_nan(row['dbgap']) else [],
            publication = str(row['publication']).split('|') if handle_nan(row['publication']) else [],
            expectedNumberOfParticipants = handle_nan(row['expected number of participants']),
            guidType = row['guid type'],
            acknowledgments = row['acknowledgments'].split('|') if handle_nan(row['acknowledgments']) else [],
            citationStatement = row['citation statement'].split('|') if handle_nan(row['citation statement']) else []
        )
        # Validation successful
        return True, None
    except ValidationError as e:
        # Validation failed
        error_details = (str(row['Study Code']), e)
        return False, error_details
