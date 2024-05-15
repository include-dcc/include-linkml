from src.data_validation.validation_utils import validate_data
from src.data_validation.validate_study import validate_study_entry
from src.data_validation.validate_participant import validate_participant_entry
from src.data_validation.validate_condition import validate_condition_entry
from src.data_validation.validate_biospecimen import validate_biospecimen_entry
from src.data_validation.validate_datafile import validate_datafile_entry
from src.data_validation.validate_dataset import validate_dataset_entry


def validate_study(file_path, output_path='.'):
    string_columns = ['Study Code', 'Program', 'Research Domain', 'Participant Lifespan Stage',
                      'Clinical Data Source Type', 'Expected Data Category', 'GUID Type']
    return validate_data(file_path, string_columns, validate_study_entry, output_path)


def validate_participant(file_path, output_path='.'):
    string_columns = ['Study Code', 'Family Type', 'Family Relationship', 'Sex', 'Race', 'Ethnicity',
                      'Down Syndrome Status', 'Outcomes Vital Status']
    return validate_data(file_path, string_columns, validate_participant_entry, output_path)


def validate_condition(file_path, output_path='.'):
    string_columns = ['Study Code', 'Condition Interpretation', 'Condition Status', 'Condition Data Source']
    return validate_data(file_path, string_columns, validate_condition_entry, output_path)


def validate_biospecimen(file_path, output_path='.'):
    string_columns = ['Study Code', 'Sample Availability', 'Container Availability']
    return validate_data(file_path, string_columns, validate_biospecimen_entry, output_path)


def validate_datafile(file_path, output_path='.'):
    string_columns = ['Study Code', 'Data Access', 'Data Category']
    return validate_data(file_path, string_columns, validate_datafile_entry, output_path)


def validate_dataset(file_path, output_path='.'):
    string_columns = ['Study Code', 'Dataset Data Category']
    return validate_data(file_path, string_columns, validate_dataset_entry, output_path)
