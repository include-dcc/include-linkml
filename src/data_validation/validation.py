from src.data_validation.validation_utils import validate_data
from src.data_validation.validate_study import validate_study_entry
from src.data_validation.validate_participant import validate_participant_entry
from src.data_validation.validate_condition import validate_condition_entry
from src.data_validation.validate_biospecimen import validate_biospecimen_entry
from src.data_validation.validate_datafile import validate_datafile_entry
from src.data_validation.validate_dataset import validate_dataset_entry
from src.data_validation.validate_datasetmanifest import validate_datasetmanifest_entry


def validate_study(file_path, output_path='.'):
    string_columns = ['study code', 'program', 'research domain', 'participant lifespan stage',
                      'clinical data source type', 'data category', 'guid type']
    return validate_data(file_path, string_columns, validate_study_entry, output_path)


def validate_participant(file_path, output_path='.'):
    string_columns = ['study code', 'family type', 'family relationship', 'sex', 'race', 'ethnicity',
                      'down syndrome status', 'outcomes vital status']
    return validate_data(file_path, string_columns, validate_participant_entry, output_path)


def validate_condition(file_path, output_path='.'):
    string_columns = ['study code', 'condition interpretation', 'condition status', 'condition data source']
    return validate_data(file_path, string_columns, validate_condition_entry, output_path)


def validate_biospecimen(file_path, output_path='.'):
    string_columns = ['study code', 'sample availability', 'container availability']
    return validate_data(file_path, string_columns, validate_biospecimen_entry, output_path)


def validate_datafile(file_path, output_path='.'):
    string_columns = ['study code', 'data access', 'data category']
    return validate_data(file_path, string_columns, validate_datafile_entry, output_path)


def validate_dataset(file_path, output_path='.'):
    string_columns = ['study code', 'data category', 'data access']
    return validate_data(file_path, string_columns, validate_dataset_entry, output_path)


def validate_datasetmanifest(file_path, output_path='.'):
    string_columns = ['study code']
    return validate_data(file_path, string_columns, validate_datasetmanifest_entry, output_path)
