import argparse
from .validation import (
    validate_study,
    validate_participant,
    validate_condition,
    validate_biospecimen,
    validate_datafile,
    validate_dataset,
    validate_datasetmanifest
)

# Dictionary to map entity names to validation functions
entity_validators = {
    'study': validate_study,
    'participant': validate_participant,
    'condition': validate_condition,
    'biospecimen': validate_biospecimen,
    'datafile': validate_datafile,
    'dataset': validate_dataset,
    'datasetmanifest': validate_datasetmanifest
}


def main():
    parser = argparse.ArgumentParser(description='Validate data from a CSV file using Pydantic models')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('-o', '--output', help='Path to the directory to save error logs')
    parser.add_argument('entity', choices=entity_validators.keys(), help='Entity to validate')
    args = parser.parse_args()

    # Print a friendly prompt to indicate processing
    print(f"Validating {args.entity} data from file: {args.input_file}")

    # Retrieve the appropriate validation function based on the specified entity
    validation_function = entity_validators[args.entity]
    validation_function(args.input_file, args.output)

    # Print a friendly message indicating completion
    print("Validation complete!")


if __name__ == "__main__":
    main()
