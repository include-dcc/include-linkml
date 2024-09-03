import pandas as pd
import os
from datetime import datetime
import chardet


def clean_string(value):
    if isinstance(value, str):
        return value.lower().replace(' ', '_').replace('-', '_').replace('/', '_')
    elif pd.isna(value):
        return None
    else:
        return str(value).lower().replace(' ', '_').replace('-', '_').replace('/', '_')


def clean_dataframe_strings(df, string_columns):
    df[string_columns] = df[string_columns].map(clean_string)


def validate_dataframe(df, entry_validator, input_file_name=None, output_path=None):
    # Check if required columns exist before validation
    try:
        validation_results = df.apply(entry_validator, axis=1)
    except KeyError as e:
        print(f"Error: Missing column - {e}")
        return 0, df.shape[0]  # All records are invalid

    valid_count = validation_results[validation_results.apply(lambda x: x[0])].shape[0]
    invalid_count = validation_results.shape[0] - valid_count
    print("Number of errors by record type:")
    for is_valid, error_info in validation_results:
        if not is_valid:
            print(f"{error_info[0]}: {str(error_info[1]).split()[0]}")
    total_records = df.shape[0]
    print(f"Total number of records in the file: {total_records}")
    print(f"Number of records with error: {invalid_count}")
    if output_path:
        output_file_path = save_validation_results(validation_results, input_file_name, output_path)
        print(f"Validation results saved to: {output_file_path}")
    return valid_count, invalid_count


def save_validation_results(validation_results, input_file_name, output_path):
    os.makedirs(output_path, exist_ok=True)
    current_date = datetime.now().strftime("%Y-%m-%d")
    output_file_name = f'{input_file_name}_validation_results_{current_date}.txt' if input_file_name else f'validation_results_{current_date}.txt'
    output_file_path = os.path.join(output_path, output_file_name)
    validation_results_str = [str(item) for item in validation_results]
    with open(output_file_path, 'w') as file:
        file.write('\n'.join(validation_results_str))
    return output_file_path

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def read_csv_file(file_path):
    encoding = detect_encoding(file_path)
    df = pd.read_csv(file_path, encoding=encoding)
    df.columns = df.columns.str.lower()  # Convert column names to lower case
    return df


def validate_data(file_path, string_columns, validation_function, output_path='.'):
    file_name = os.path.basename(file_path)
    df = read_csv_file(file_path)
    clean_dataframe_strings(df, string_columns)
    valid_count, invalid_count = validate_dataframe(df, validation_function, input_file_name=file_name,
                                                    output_path=output_path)
    return valid_count, invalid_count

def handle_nan(value):
    """Convert NaN values to None"""
    if pd.isna(value):
        return None
    return value
