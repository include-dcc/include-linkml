# LinkML Schema Linting and Validation

This project uses [LinkML](https://linkml.io/) to define schemas and validate tabular data files. Below are the commands used to lint and validate schemas and data using `linkml-lint` and `linkml-validate`.

---

## 🔍 Schema Linting

We use `linkml-lint` to check for syntax and structure issues in the schema.

### 1. Full Linting Check

```bash
linkml-lint src/linkml/include_schema.yaml
```
- **More Info**: [linkml-lint CLI](https://linkml.io/linkml/cli/lint.html)

✅ Data Validation
-----------------

We use `linkml-validate` to check whether data files conform to their schema definitions.

### 1. Validate `study.csv` against `Study` class
```bash
linkml-validate -s src/linkml/include_schema.yaml -C Study src/data/input/study.csv
```
### 2. Validate `participant.csv` against `Participant` class
```bash
linkml-validate -s src/linkml/include_schema.yaml -C Participant src/data/input/participant.csv
```
### 3. Validate `condition.csv` against `Condition` class
```bash
linkml-validate -s src/linkml/include_schema.yaml -C Condition src/data/input/condition.csv
```
### 4. Validate `biospecimen.csv` against `Biospecimen` class
```bash
linkml-validate -s src/linkml/include_schema.yaml -C Biospecimen src/data/input/biospecimen.csv
```
### 5. Validate `datafile.csv` against `DataFile` class
```bash
linkml-validate -s src/linkml/include_schema.yaml -C DataFile src/data/input/datafile.csv
```

- **More Info**: [linkml-validate CLI](https://linkml.io/linkml/cli/validate.html) 

### 📤 Saving Validation Logs

To save validation output to a file (e.g., for documentation or reporting), redirect the output of `linkml-validate`:

```bash
linkml-validate -s src/linkml/include_schema.yaml -C Study src/data/input/study.csv > src/data/output/validation-report.md
```
You can change the extension to .csv, .txt, or .json based on your preferred format.

📌 Notes
    
- Ensure all required fields are present in your CSV files.
    
- Column names in SCV files must match the schema slot names.
    
- The schema file (src/linkml/include_schema.yaml) must define all referenced classes (Study, Participant, etc.).