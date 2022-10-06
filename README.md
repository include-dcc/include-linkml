# INCLUDE v2 LinkML Data Model

This repository includes the LinkML model and tooling for the v2 Data Model







# Poetry Environment
This repo requires poetry as a system dependency

https://python-poetry.org/docs/#installation

When poetry is installed run:
`poetry install`




# Workflow to update the model from:
## [INCLUDE Schemasheets Google Sheets Project](https://docs.google.com/spreadsheets/d/1w6zDfz3_yrCjjrqfpXBGNmd0LZL4B03gr1KfzJtk5Cs/edit?usp=sharing)
1. Pull latest changes from GSheets project and update the .tsv files located at src/data/sheets

`cogs pull`

2. Run the sheets2linkml command to push changes to the yaml model file located at src/linkml/include_linkml.yaml

`sheets2linkml -o src/linkml/include_linkml.yaml src/data/sheets/*.tsv`

3. Run the Schematic JSON-LD transformer to generate the JSON-LD that Schematic will use to generate Manifests

`poetry run python src/schematic/json_transformer.py`

4. Run Schematic configured to point at the generated json-ld at src/schematic/include_schematic_linkml.jsonld

`schematic manifest --config /Users/putmanti/CODE/schematic/schematic/config.yml get -s`